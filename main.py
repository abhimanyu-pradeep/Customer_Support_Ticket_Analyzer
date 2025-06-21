import json
from agents.base_agent import Ticket, AgentOutput
from agents.technical_analyzer import TechnicalAnalyzerAgent
from agents.customer_context import CustomerContextAgent
from evaluation.evaluator import evaluate_system
from evaluation.test_cases import get_test_cases

def process_ticket(ticket_data: dict) -> AgentOutput:
    """
    Processes a single support ticket using multiple specialized agents
    and an orchestration layer to determine final routing.

    Args:
        ticket_data (dict): A dictionary containing raw ticket information.

    Returns:
        AgentOutput: The final aggregated analysis and routing decision.
    """
    try:
        # Validate and parse the input ticket data using Pydantic model
        ticket = Ticket(**ticket_data)
    except Exception as e:
        print(f"Error validating ticket input: {e}")
        # Return a default error output or raise the exception
        return AgentOutput(
            category="Error",
            priority="Critical", # Mark as critical for immediate review
            recommended_team="System Admin",
            reasoning=f"Failed to parse ticket input: {e}"
        )

    print(f"\nProcessing Ticket ID: {ticket.ticket_id}")

    # Initialize specialized agents
    technical_agent = TechnicalAnalyzerAgent()
    customer_agent = CustomerContextAgent()

    # Get analyses from each agent
    # We pass the full ticket object to each agent for their specialized analysis
    tech_analysis: AgentOutput = technical_agent.analyze(ticket)
    cust_analysis: AgentOutput = customer_agent.analyze(ticket)

    print(f"  Technical Agent Analysis: Category='{tech_analysis.category}', Priority='{tech_analysis.priority}', Team='{tech_analysis.recommended_team}'")
    print(f"  Customer Agent Analysis: Category='{cust_analysis.category}', Priority='{cust_analysis.priority}', Team='{cust_analysis.recommended_team}'")

    # --- Orchestration and Conflict Resolution Logic ---
    # Define a mapping for priority levels to allow numeric comparison
    priority_map = {
        "Info": 1,
        "Low": 2,
        "Medium": 3,
        "High": 4,
        "Critical": 5
    }

    # Determine final priority: Take the highest priority suggested by any agent
    final_priority_value = max(
        priority_map.get(tech_analysis.priority, 1),
        priority_map.get(cust_analysis.priority, 1)
    )
    final_priority = next(
        (p_name for p_name, p_val in priority_map.items() if p_val == final_priority_value),
        "Medium" # Default if not found, though it should be
    )

    # Determine final category and recommended team
    final_category: str = "General Inquiry"
    final_recommended_team: str = "Support Tier 1"
    final_reasoning: str = ""

    # Prioritize technical issues if identified by the Technical Analyzer
    if "Technical" in tech_analysis.category:
        final_category = tech_analysis.category
        final_recommended_team = tech_analysis.recommended_team
    elif "Urgent Customer Issue" in cust_analysis.category:
        # If not technical, check for urgent customer-related issues
        final_category = cust_analysis.category
        final_recommended_team = cust_analysis.recommended_team
    else:
        # Fallback to customer agent's general category or a default
        if cust_analysis.category != "General Inquiry":
            final_category = cust_analysis.category
            final_recommended_team = cust_analysis.recommended_team
        else:
            final_category = tech_analysis.category # Use technical agent's general category if customer agent didn't find specific category.
            final_recommended_team = tech_analysis.recommended_team


    # Combine reasoning from both agents
    final_reasoning = (
        f"Technical perspective: {tech_analysis.reasoning}\n"
        f"Customer context perspective: {cust_analysis.reasoning}\n"
        f"Orchestration decision: Final priority is '{final_priority}' "
        f"based on maximum urgency. Final routing to '{final_category}' "
        f"with '{final_recommended_team}' recommended team."
    )

    final_output = AgentOutput(
        category=final_category,
        priority=final_priority,
        recommended_team=final_recommended_team,
        reasoning=final_reasoning
    )

    print(f"  Final Decision: Category='{final_output.category}', Priority='{final_output.priority}', Team='{final_output.recommended_team}'")
    return final_output


if __name__ == "__main__":
    print("--- Starting Multi-Agent Ticket Analysis System ---")

    # Get test cases
    test_cases = get_test_cases()

    # Process each test case and print results
    print("\n--- Running Individual Test Cases ---")
    results = []
    for i, test_case in enumerate(test_cases):
        print(f"\n--- Test Case {i+1} ---")
        ticket_id = test_case.get("ticket_id", "N/A")
        print(f"Input Ticket: {json.dumps(test_case, indent=2)}")
        final_analysis = process_ticket(test_case)
        results.append(final_analysis)
        print(f"\nFinal Analyzed Output for Ticket {ticket_id}:")
        print(final_analysis.model_dump_json(indent=2))

    # Evaluate the system performance on all test cases
    print("\n--- Evaluating System Performance ---")
    evaluation_results = evaluate_system(test_cases, process_ticket)
    print("\nEvaluation Summary:")
    for metric, value in evaluation_results.items():
        print(f"- {metric}: {value}")

    print("\n--- Multi-Agent System Execution Complete ---")