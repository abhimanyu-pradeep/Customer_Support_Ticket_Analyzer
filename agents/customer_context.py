from agents.base_agent import BaseAgent, Ticket, AgentOutput

class CustomerContextAgent(BaseAgent):
    """
    Specialized agent focused on analyzing the customer's context (tier, revenue,
    previous tickets, account age) to determine business impact and priority.
    """
    def analyze(self, ticket: Ticket) -> AgentOutput:
        """
        Analyzes customer attributes to assess priority and suggest appropriate
        customer-facing team.
        """
        category = "General Inquiry"
        priority = "Low"
        recommended_team = "Customer Success"
        reasoning = []

        # --- Priority Determination based on Customer Tier ---
        if ticket.customer_tier == "enterprise":
            priority = "High"
            reasoning.append("Enterprise customer, elevating priority.")
        elif ticket.customer_tier == "premium":
            if priority != "High": # Don't downgrade if already high
                priority = "Medium"
                reasoning.append("Premium customer, elevating priority to Medium.")
        elif ticket.customer_tier == "free":
            if priority == "Low": # Ensure it doesn't get downgraded from technical agent's assessment
                priority = "Low"
            reasoning.append("Free tier customer.")

        # --- Priority Adjustment based on Monthly Revenue ---
        if ticket.monthly_revenue >= 10000:
            if priority == "Medium": priority = "High"
            elif priority == "Low": priority = "Medium"
            reasoning.append(f"High monthly revenue (${ticket.monthly_revenue}), further elevating priority.")
        elif ticket.monthly_revenue >= 1000:
            # Maintain current priority
            reasoning.append(f"Medium monthly revenue (${ticket.monthly_revenue}).")
        else:
            if priority == "Medium": priority = "Low" # Only lower if not High/Critical
            reasoning.append(f"Low monthly revenue (${ticket.monthly_revenue}).")

        # --- Priority Adjustment based on Previous Tickets ---
        if ticket.previous_tickets >= 5:
            if priority == "Medium": priority = "High"
            elif priority == "Low": priority = "Medium"
            reasoning.append(f"Many previous tickets ({ticket.previous_tickets}), indicates potential chronic issue or frustrated customer, elevating priority.")
        elif ticket.previous_tickets >= 2:
            reasoning.append(f"Some previous tickets ({ticket.previous_tickets}).")
        else:
            reasoning.append(f"Few previous tickets ({ticket.previous_tickets}).")

        # --- Category and Team Determination ---
        if "billing" in ticket.subject.lower() or "payment" in ticket.message.lower():
            category = "Billing Inquiry"
            recommended_team = "Billing Support"
            reasoning.append("Detected billing-related keywords.")
        elif "account" in ticket.subject.lower() or "login" in ticket.message.lower() or "password" in ticket.subject.lower():
            category = "Account Management"
            recommended_team = "Customer Success"
            reasoning.append("Detected account management keywords.")
        elif priority in ["High", "Critical"] and ticket.customer_tier in ["premium", "enterprise"]:
            category = "Urgent Customer Issue"
            recommended_team = "Account Manager"
            reasoning.append("Urgent issue for high-value customer, recommending Account Manager.")
        else:
            category = "General Inquiry"
            recommended_team = "Customer Success"
            reasoning.append("General customer inquiry.")

        return AgentOutput(
            category=category,
            priority=priority,
            recommended_team=recommended_team,
            reasoning="Customer context analysis: " + " ".join(reasoning)
        )