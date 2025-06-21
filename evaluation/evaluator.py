from typing import List, Dict, Callable
from agents.base_agent import Ticket, AgentOutput
from agents.technical_analyzer import TechnicalAnalyzerAgent
from agents.customer_context import CustomerContextAgent

def evaluate_system(
    test_cases: List[Dict],
    process_ticket_func: Callable[[Dict], AgentOutput]
) -> Dict[str, float]:
    """
    Evaluates the performance of the multi-agent system using various metrics.

    Args:
        test_cases (List[Dict]): A list of raw ticket dictionaries to evaluate.
        process_ticket_func (Callable): The main function to process a ticket,
                                        which orchestrates the agents.

    Returns:
        Dict[str, float]: A dictionary containing the calculated metrics.
    """
    results_summary = {
        "total_tickets": len(test_cases),
        "inter_agent_category_agreement_rate": 0,
        "inter_agent_priority_agreement_rate": 0,
        "output_completeness_rate": 0,
        "avg_reasoning_length": 0,
        "simulated_correctness_score": 0 # This will be based on heuristic for this simulation
    }

    category_agreements = 0
    priority_agreements = 0
    complete_outputs = 0
    total_reasoning_length = 0
    simulated_correctness_score = 0

    technical_agent = TechnicalAnalyzerAgent()
    customer_agent = CustomerContextAgent()

    for test_case_data in test_cases:
        # Re-parse ticket for individual agent analysis (for agreement calculation)
        ticket = Ticket(**test_case_data)

        tech_analysis = technical_agent.analyze(ticket)
        cust_analysis = customer_agent.analyze(ticket)

        # Calculate inter-agent agreement
        if tech_analysis.category == cust_analysis.category:
            category_agreements += 1
        if tech_analysis.priority == cust_analysis.priority:
            priority_agreements += 1

        # Process the ticket through the full orchestrated system
        final_output = process_ticket_func(test_case_data)

        # Check output completeness
        if all(
            getattr(final_output, field) is not None and getattr(final_output, field) != ""
            for field in AgentOutput.model_fields.keys()
        ):
            complete_outputs += 1

        # Sum reasoning length for average calculation
        total_reasoning_length += len(final_output.reasoning)

        # --- Simulated Correctness Score (Heuristic-based for this example) ---
        # This is a very simple heuristic. In a real system, this would involve
        # comparing to manually labeled ground truth.
        score = 0
        # High score for high priority tickets from high-value customers
        if ticket.customer_tier in ["enterprise", "premium"] and final_output.priority in ["High", "Critical"]:
            score += 1

        # Score for correct technical routing if the subject/message implies technicality
        if "error" in ticket.subject.lower() or "failing" in ticket.message.lower():
            if "Technical" in final_output.category and final_output.recommended_team in ["Engineering", "DevOps"]:
                score += 1

        # Score for correct customer service routing if it's a general inquiry
        if "question" in ticket.subject.lower() and final_output.recommended_team == "Customer Success":
             score += 1

        simulated_correctness_score += score


    results_summary["inter_agent_category_agreement_rate"] = (
        category_agreements / results_summary["total_tickets"]
    ) if results_summary["total_tickets"] > 0 else 0
    results_summary["inter_agent_priority_agreement_rate"] = (
        priority_agreements / results_summary["total_tickets"]
    ) if results_summary["total_tickets"] > 0 else 0
    results_summary["output_completeness_rate"] = (
        complete_outputs / results_summary["total_tickets"]
    ) if results_summary["total_tickets"] > 0 else 0
    results_summary["avg_reasoning_length"] = (
        total_reasoning_length / results_summary["total_tickets"]
    ) if results_summary["total_tickets"] > 0 else 0
    results_summary["simulated_correctness_score"] = (
        simulated_correctness_score / results_summary["total_tickets"]
    ) if results_summary["total_tickets"] > 0 else 0


    return results_summary
