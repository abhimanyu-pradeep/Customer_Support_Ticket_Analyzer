from typing import List, Dict

def get_test_cases() -> List[Dict]:
    """
    Returns a list of predefined test cases (raw ticket data) for evaluation.
    These cases cover different scenarios and customer profiles.
    """
    test_cases = [
        {
            "ticket_id": "1001",
            "customer_tier": "premium",
            "subject": "API returning 500 errors intermittently",
            "message": "Hi, our production system has been failing for the last hour due to intermittent 500 errors from your user API. We need an urgent fix.",
            "previous_tickets": 3,
            "monthly_revenue": 5000.0,
            "account_age_days": 450
        },
        {
            "ticket_id": "SUP-001",
            "customer_tier": "free",
            "subject": "This product is completely broken!!!",
            "message": "Nothing works! I can't even log in. This is the worst software I've ever used.", 
            "previous_tickets": 0,
            "monthly_revenue": 0,
            "account_age_days": 2
        },
        {
            "ticket_id": "SUP-002",
            "customer_tier": "enterprise",
            "subject": "Minor UI issue with dashboard",
            "message": "Hi team, just noticed the dashboard numbers are slightly misaligned on mobile view",
            "previous_tickets": 15,
            "monthly_revenue": 25000,
            "account_age_days": 730
        },
        {
            "ticket_id": "SUP-003",
            "customer_tier": "premium",
            "subject": "Feature Request: Bulk export",
            "message": "We need bulk export functionality for our quarterly reports.",
            "previous_tickets": 5,
            "monthly_revenue": 5000,
            "account_age_days": 400
        },
        {
            "ticket_id": "SUP-004",
            "customer_tier": "premium",
            "subject": "API rate limits unclear",
            "message": "Getting rate limited but documentation says we should have 1000 requests/hour.",
            "previous_tickets": 8,
            "monthly_revenue": 3000,
            "account_age_days": 180
        },
        {
            "ticket_id": "SUP-005",
            "customer_tier": "enterprise",
            "subject": "Urgent: Security vulnerability?",
            "message": "Our security team flagged that your API responses include internal server paths",
            "previous_tickets": 20,
            "monthly_revenue": 50000,
            "account_age_days": 900
        },
        {
            "ticket_id": "1007",
            "customer_tier": "premium",
            "subject": "Frontend rendering glitch on dashboard",
            "message": "The main dashboard is not loading correctly for me. Some elements are overlapping. I'm using Chrome browser.",
            "previous_tickets": 0,
            "monthly_revenue": 3000.0,
            "account_age_days": 200
        }
    ]
    return test_cases

'''
--- Starting Multi-Agent Ticket Analysis System ---

--- Running Individual Test Cases ---

--- Test Case 1 ---
Input Ticket: {
  "ticket_id": "1001",
  "customer_tier": "premium",
  "subject": "API returning 500 errors intermittently",
  "message": "Hi, our production system has been failing for the last hour due to intermittent 500 errors from your user API. We need an urgent fix.",
  "previous_tickets": 3,
  "monthly_revenue": 5000.0,
  "account_age_days": 450
}

Processing Ticket ID: 1001
  Technical Agent Analysis: Category='Technical - API', Priority='High', Team='Engineering'
  Customer Agent Analysis: Category='General Inquiry', Priority='Medium', Team='Customer Success'
  Final Decision: Category='Technical - API', Priority='High', Team='Engineering'

Final Analyzed Output for Ticket 1001:
{
  "category": "Technical - API",
  "priority": "High",
  "recommended_team": "Engineering",
  "reasoning": "Technical perspective: Technical analysis: Detected API-related keywords. Detected high impact keywords. Issue requires Engineering expertise.\nCustomer context perspective: Customer context analysis: Premium customer, elevating priority to Medium. Medium monthly revenue ($5000.0). Some previous tickets (3). General customer inquiry.\nOrchestration decision: Final priority is 'High' based on maximum urgency. Final routing to 'Technical - API' with 'Engineering' recommended team."
}

--- Test Case 2 ---
Input Ticket: {
  "ticket_id": "SUP-001",
  "customer_tier": "free",
  "subject": "This product is completely broken!!!",
  "message": "Nothing works! I can't even log in. This is the worst software I've ever used.",
  "previous_tickets": 0,
  "monthly_revenue": 0,
  "account_age_days": 2
}

Processing Ticket ID: SUP-001
  Technical Agent Analysis: Category='General Technical', Priority='Medium', Team='Support Tier 2'
  Customer Agent Analysis: Category='General Inquiry', Priority='Low', Team='Customer Success'
  Final Decision: Category='General Technical', Priority='Medium', Team='Support Tier 2'

Final Analyzed Output for Ticket SUP-001:
{
  "category": "General Technical",
  "priority": "Medium",
  "recommended_team": "Support Tier 2",
  "reasoning": "Technical perspective: Technical analysis: General technical issue for Tier 2 support.\nCustomer context perspective: Customer context analysis: Free tier customer. Low monthly revenue ($0.0). Few previous tickets (0). General customer inquiry.\nOrchestration decision: Final priority is 'Medium' based on maximum urgency. Final routing to 'General Technical' with 'Support Tier 2' recommended team."
}

--- Test Case 3 ---
Input Ticket: {
  "ticket_id": "SUP-002",
  "customer_tier": "enterprise",
  "subject": "Minor UI issue with dashboard",
  "message": "Hi team, just noticed the dashboard numbers are slightly misaligned on mobile view",
  "previous_tickets": 15,
  "monthly_revenue": 25000,
  "account_age_days": 730
}

Processing Ticket ID: SUP-002
  Technical Agent Analysis: Category='Technical - Frontend/UI', Priority='Medium', Team='DevOps'
  Customer Agent Analysis: Category='Urgent Customer Issue', Priority='High', Team='Account Manager'
  Final Decision: Category='Technical - Frontend/UI', Priority='High', Team='DevOps'

Final Analyzed Output for Ticket SUP-002:
{
  "category": "Technical - Frontend/UI",
  "priority": "High",
  "recommended_team": "DevOps",
  "reasoning": "Technical perspective: Technical analysis: Detected frontend/UI-related keywords. Issue suitable for DevOps/IT Support.\nCustomer context perspective: Customer context analysis: Enterprise customer, elevating priority. High monthly revenue ($25000.0), further elevating priority. Many previous tickets (15), indicates potential chronic issue or frustrated customer, elevating priority. Urgent issue for high-value customer, recommending Account Manager.\nOrchestration decision: Final priority is 'High' based on maximum urgency. Final routing to 'Technical - Frontend/UI' with 'DevOps' recommended team."
}

--- Test Case 4 ---
Input Ticket: {
  "ticket_id": "SUP-003",
  "customer_tier": "premium",
  "subject": "Feature Request: Bulk export",
  "message": "We need bulk export functionality for our quarterly reports.",
  "previous_tickets": 5,
  "monthly_revenue": 5000,
  "account_age_days": 400
}

Processing Ticket ID: SUP-003
  Technical Agent Analysis: Category='Technical - API', Priority='Low', Team='Engineering'
  Customer Agent Analysis: Category='Urgent Customer Issue', Priority='High', Team='Account Manager'
  Final Decision: Category='Technical - API', Priority='High', Team='Engineering'

Final Analyzed Output for Ticket SUP-003:
{
  "category": "Technical - API",
  "priority": "High",
  "recommended_team": "Engineering",
  "reasoning": "Technical perspective: Technical analysis: Detected API-related keywords. Detected low impact/informational keywords. Issue requires Engineering expertise.\nCustomer context perspective: Customer context analysis: Premium customer, elevating priority to Medium. Medium monthly revenue ($5000.0). Many previous tickets (5), indicates potential chronic issue or frustrated customer, elevating priority. Urgent issue for high-value customer, recommending Account Manager.\nOrchestration decision: Final priority is 'High' based on maximum urgency. Final routing to 'Technical - API' with 'Engineering' recommended team."
}

--- Test Case 5 ---
Input Ticket: {
  "ticket_id": "SUP-004",
  "customer_tier": "premium",
  "subject": "API rate limits unclear",
  "message": "Getting rate limited but documentation says we should have 1000 requests/hour.",
  "previous_tickets": 8,
  "monthly_revenue": 3000,
  "account_age_days": 180
}

Processing Ticket ID: SUP-004
  Technical Agent Analysis: Category='Technical - API', Priority='Medium', Team='Engineering'
  Customer Agent Analysis: Category='Urgent Customer Issue', Priority='High', Team='Account Manager'
  Final Decision: Category='Technical - API', Priority='High', Team='Engineering'

Final Analyzed Output for Ticket SUP-004:
{
  "category": "Technical - API",
  "priority": "High",
  "recommended_team": "Engineering",
  "reasoning": "Technical perspective: Technical analysis: Detected API-related keywords. Issue requires Engineering expertise.\nCustomer context perspective: Customer context analysis: Premium customer, elevating priority to Medium. Medium monthly revenue ($3000.0). Many previous tickets (8), indicates potential chronic issue or frustrated customer, elevating priority. Urgent issue for high-value customer, recommending Account Manager.\nOrchestration decision: Final priority is 'High' based on maximum urgency. Final routing to 'Technical - API' with 'Engineering' recommended team."
}

--- Test Case 6 ---
Input Ticket: {
  "ticket_id": "SUP-005",
  "customer_tier": "enterprise",
  "subject": "Urgent: Security vulnerability?",
  "message": "Our security team flagged that your API responses include internal server paths",
  "previous_tickets": 20,
  "monthly_revenue": 50000,
  "account_age_days": 900
}

Processing Ticket ID: SUP-005
  Technical Agent Analysis: Category='Technical - API', Priority='Medium', Team='Engineering'
  Customer Agent Analysis: Category='Urgent Customer Issue', Priority='High', Team='Account Manager'
  Final Decision: Category='Technical - API', Priority='High', Team='Engineering'

Final Analyzed Output for Ticket SUP-005:
{
  "category": "Technical - API",
  "priority": "High",
  "recommended_team": "Engineering",
  "reasoning": "Technical perspective: Technical analysis: Detected API-related keywords. Issue requires Engineering expertise.\nCustomer context perspective: Customer context analysis: Enterprise customer, elevating priority. High monthly revenue ($50000.0), further elevating priority. Many previous tickets (20), indicates potential chronic issue or frustrated customer, elevating priority. Urgent issue for high-value customer, recommending Account Manager.\nOrchestration decision: Final priority is 'High' based on maximum urgency. Final routing to 'Technical - API' with 'Engineering' recommended team."
}

--- Test Case 7 ---
Input Ticket: {
  "ticket_id": "1007",
  "customer_tier": "premium",
  "subject": "Frontend rendering glitch on dashboard",
  "message": "The main dashboard is not loading correctly for me. Some elements are overlapping. I'm using Chrome browser.",
  "previous_tickets": 0,
  "monthly_revenue": 3000.0,
  "account_age_days": 200
}

Processing Ticket ID: 1007
  Technical Agent Analysis: Category='Technical - Frontend/UI', Priority='Medium', Team='DevOps'
  Customer Agent Analysis: Category='General Inquiry', Priority='Medium', Team='Customer Success'
  Final Decision: Category='Technical - Frontend/UI', Priority='Medium', Team='DevOps'

Final Analyzed Output for Ticket 1007:
{
  "category": "Technical - Frontend/UI",
  "priority": "Medium",
  "recommended_team": "DevOps",
  "reasoning": "Technical perspective: Technical analysis: Detected frontend/UI-related keywords. Issue suitable for DevOps/IT Support.\nCustomer context perspective: Customer context analysis: Premium customer, elevating priority to Medium. Medium monthly revenue ($3000.0). Few previous tickets (0). General customer inquiry.\nOrchestration decision: Final priority is 'Medium' based on maximum urgency. Final routing to 'Technical - Frontend/UI' with 'DevOps' recommended team."
}

--- Evaluating System Performance ---

Processing Ticket ID: 1001
  Technical Agent Analysis: Category='Technical - API', Priority='High', Team='Engineering'
  Customer Agent Analysis: Category='General Inquiry', Priority='Medium', Team='Customer Success'
  Final Decision: Category='Technical - API', Priority='High', Team='Engineering'

Processing Ticket ID: SUP-001
  Technical Agent Analysis: Category='General Technical', Priority='Medium', Team='Support Tier 2'
  Customer Agent Analysis: Category='General Inquiry', Priority='Low', Team='Customer Success'
  Final Decision: Category='General Technical', Priority='Medium', Team='Support Tier 2'

Processing Ticket ID: SUP-002
  Technical Agent Analysis: Category='Technical - Frontend/UI', Priority='Medium', Team='DevOps'
  Customer Agent Analysis: Category='Urgent Customer Issue', Priority='High', Team='Account Manager'
  Final Decision: Category='Technical - Frontend/UI', Priority='High', Team='DevOps'

Processing Ticket ID: SUP-003
  Technical Agent Analysis: Category='Technical - API', Priority='Low', Team='Engineering'
  Customer Agent Analysis: Category='Urgent Customer Issue', Priority='High', Team='Account Manager'
  Final Decision: Category='Technical - API', Priority='High', Team='Engineering'

Processing Ticket ID: SUP-004
  Technical Agent Analysis: Category='Technical - API', Priority='Medium', Team='Engineering'
  Customer Agent Analysis: Category='Urgent Customer Issue', Priority='High', Team='Account Manager'
  Final Decision: Category='Technical - API', Priority='High', Team='Engineering'

Processing Ticket ID: SUP-005
  Technical Agent Analysis: Category='Technical - API', Priority='Medium', Team='Engineering'
  Customer Agent Analysis: Category='Urgent Customer Issue', Priority='High', Team='Account Manager'
  Final Decision: Category='Technical - API', Priority='High', Team='Engineering'

Processing Ticket ID: 1007
  Technical Agent Analysis: Category='Technical - Frontend/UI', Priority='Medium', Team='DevOps'
  Customer Agent Analysis: Category='General Inquiry', Priority='Medium', Team='Customer Success'
  Final Decision: Category='Technical - Frontend/UI', Priority='Medium', Team='DevOps'

Evaluation Summary:
- total_tickets: 7
- inter_agent_category_agreement_rate: 0.0
- inter_agent_priority_agreement_rate: 0.14285714285714285
- output_completeness_rate: 1.0
- avg_reasoning_length: 531.0
- simulated_correctness_score: 0.8571428571428571

--- Multi-Agent System Execution Complete ---
'''