from agents.base_agent import BaseAgent, Ticket, AgentOutput

class TechnicalAnalyzerAgent(BaseAgent):
    """
    Specialized agent focused on analyzing the technical aspects of a support ticket.
    Determines category, priority, and recommended team based on technical keywords
    in the subject and message.
    """
    def analyze(self, ticket: Ticket) -> AgentOutput:
        """
        Analyzes the ticket's subject and message for technical keywords
        to determine technical category, priority, and recommended team.
        """
        subject_lower = ticket.subject.lower()
        message_lower = ticket.message.lower()
        combined_text = subject_lower + " " + message_lower

        category = "General Technical"
        priority = "Medium"
        recommended_team = "Support Tier 2"
        reasoning = []

        # --- Category Determination ---
        if any(keyword in combined_text for keyword in ["api", "endpoint", "integration", "sdk", "webhook", "rest", "graphql", "request", "response", "status code", "500", "404", "authentication", "authorization"]):
            category = "Technical - API"
            reasoning.append("Detected API-related keywords.")
        elif any(keyword in combined_text for keyword in ["database", "db", "sql", "nosql", "query", "schema", "migration", "data loss", "performance slow", "corrupt data"]):
            category = "Technical - Database"
            reasoning.append("Detected database-related keywords.")
        elif any(keyword in combined_text for keyword in ["ui", "ux", "frontend", "website", "dashboard", "button", "layout", "rendering", "browser", "css", "javascript", "react", "angular", "vue"]):
            category = "Technical - Frontend/UI"
            reasoning.append("Detected frontend/UI-related keywords.")
        elif any(keyword in combined_text for keyword in ["service", "server", "microservice", "logic", "computation", "timeout", "latency", "deployment"]):
            category = "Technical - Backend/Service"
            reasoning.append("Detected backend/service-related keywords.")
        elif any(keyword in combined_text for keyword in ["network", "connectivity", "firewall", "vpn", "dns"]):
            category = "Technical - Network"
            reasoning.append("Detected network-related keywords.")

        # --- Priority Determination ---
        if any(keyword in combined_text for keyword in ["production down", "critical", "blocking", "major outage", "all users affected", "data loss", "security breach"]):
            priority = "Critical"
            reasoning.append("Detected critical impact keywords.")
        elif any(keyword in combined_text for keyword in ["intermittent", "significant impact", "many users", "degraded performance", "unable to complete task"]):
            if priority != "Critical": # Don't downgrade if already critical
                priority = "High"
                reasoning.append("Detected high impact keywords.")
        elif any(keyword in combined_text for keyword in ["minor issue", "bug", "improvement", "one user affected"]):
            if priority == "Medium" or priority == "Low": # Only downgrade if not already high/critical
                priority = "Medium"
                reasoning.append("Detected medium impact keywords.")
        elif any(keyword in combined_text for keyword in ["question", "suggestion", "feature request", "cosmetic"]):
            priority = "Low"
            reasoning.append("Detected low impact/informational keywords.")

        # --- Recommended Team Determination ---
        if priority == "Critical" or "API" in category or "Database" in category or "Backend" in category:
            recommended_team = "Engineering"
            reasoning.append("Issue requires Engineering expertise.")
        elif "Frontend" in category or "Network" in category:
            recommended_team = "DevOps" # Or dedicated "IT Support" depending on org structure
            reasoning.append("Issue suitable for DevOps/IT Support.")
        else:
            recommended_team = "Support Tier 2"
            reasoning.append("General technical issue for Tier 2 support.")


        return AgentOutput(
            category=category,
            priority=priority,
            recommended_team=recommended_team,
            reasoning="Technical analysis: " + " ".join(reasoning)
        )