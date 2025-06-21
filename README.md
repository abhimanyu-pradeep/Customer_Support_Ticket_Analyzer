# Multi-Agent Customer Support Ticket Analyzer

This repository presents a simple but powerful multi-agent system built to automatically analyze incoming customer support tickets. By combining the strengths of specialized AI agents, it classifies each ticket by category, determines its priority, and recommends the most appropriate team for routing.

Built using **Pydantic AI** for structured data handling, the project also includes a lightweight evaluation framework and simulated test cases—making it an ideal case study in agent collaboration, system orchestration, and modular AI design.

---

## Project Structure

main_directory_name/
├── main.py # Orchestrator and entry point
├── agents/ # Specialized agent logic lives here
│ ├── init.py
│ ├── base_agent.py # Pydantic models and BaseAgent class
│ ├── technical_analyzer.py # Handles technical issues
│ └── customer_context.py # Handles customer-related context
├── evaluation/
│ ├── init.py
│ ├── evaluator.py # Metrics and scoring logic
│ └── test_cases.py # Sample tickets for evaluation
├── docs/
│ ├── architecture.md # System architecture and agent interaction
│ └── design_decisions.md # Why we built it this way
└── README.md # Project overview and execution guide

## Getting Started

### 1. Setup

Clone the repository (conceptually, since code is shared directly):

```bash
# git clone <your-repo-url>
# cd main_directory_name

Install dependencies:
pip install pydantic

Run the application:
python main.py

The script will run predefined test cases and print out both results and an evaluation summary.

## Evaluation Framework

The `evaluation/evaluator.py` script provides a basic yet insightful way to assess the performance of the multi-agent ticket analysis system. It focuses on evaluating agent agreement, output quality, and decision consistency using predefined test cases.

### Metrics Implemented

#### 1. Inter-Agent Category Agreement Rate

- **Definition:**  
  The percentage of test cases where both the `TechnicalAnalyzerAgent` and the `CustomerContextAgent` independently identify the same ticket category before orchestration.

- **Purpose:**  
  Measures how aligned the agents are in classifying the core issue. A low agreement rate may highlight distinct perspectives or indicate a need to refine agent roles.

---

#### 2. Inter-Agent Priority Agreement Rate

- **Definition:**  
  The percentage of test cases where both agents agree on the urgency (priority) of the ticket.

- **Purpose:**  
  Evaluates how consistently urgency is assessed. Differences are expected due to the distinct focuses of the agents, but major discrepancies help validate the orchestrator's conflict resolution logic.

---

#### 3. Output Completeness Rate

- **Definition:**  
  The percentage of orchestrated outputs that include all required fields: `category`, `priority`, `recommended_team`, and `reasoning`.

- **Purpose:**  
  Serves as a quality control metric to ensure the system always generates complete, usable outputs regardless of input conditions.

---

#### 4. Average Reasoning Length

- **Definition:**  
  The average number of characters in the `reasoning` field of the final output.

- **Purpose:**  
  Acts as a proxy for the richness of explanation. Longer reasoning is often more informative for human reviewers, helping them understand why a ticket was routed a certain way.

---

#### 5. Simulated Correctness Score

- **Definition:**  
  A heuristic-based score approximating how "reasonable" the final decision is, based on expected rules from the test cases.

- **Purpose:**  
  Since ground-truth labels are unavailable, this score provides an indicative measure of how well the system performs under expected logic—for example, ensuring critical tickets from enterprise clients are treated with high priority.

---

### Consistency Management

While agents are not required to agree on their individual outputs, the **orchestrator** plays a crucial role in resolving inconsistencies. It merges agent suggestions into a unified output, applying rules such as:

- Always selecting the highest priority.
- Favoring technical categorizations when applicable.
- Incorporating customer impact when prioritizing urgency.

The agreement metrics serve as indicators of how aligned the agents naturally are, helping to fine-tune agent responsibilities if necessary.

---

## Example Test Case Behavior

### Ticket ID: SUP-001 — Login Failure (Free User)

- **Technical Agent:** Critical technical issue (backend failure).  
- **Customer Agent:** Low priority (free-tier, new user).  
- **Orchestrator:** Prioritizes technical severity.  
- **Final Decision:** `Technical - Backend/Service`, `Critical`, `Engineering`

---

### Ticket ID: SUP-002 — UI Bug (Enterprise Client)

- **Technical Agent:** Minor UI issue.  
- **Customer Agent:** High-value client with a history of tickets.  
- **Orchestrator:** Elevates based on customer context.  
- **Final Decision:** `Urgent Customer Issue`, `High`, `Account Manager`

---

### Ticket ID: SUP-003 — Feature Request (Premium)

- **Technical Agent:** Low priority general technical request.  
- **Customer Agent:** Premium tier bumps it to Medium.  
- **Orchestrator:** Accepts elevated priority, retains technical routing.  
- **Final Decision:** `General Technical`, `Medium`, `Support Tier 2`

---

### Ticket ID: SUP-004 — API Rate Limit (Premium)

- **Technical Agent:** Medium priority technical issue.  
- **Customer Agent:** High-value client with recurring issues.  
- **Orchestrator:** Elevates priority, retains technical focus.  
- **Final Decision:** `Technical - API`, `High`, `Engineering`

---

### Ticket ID: SUP-005 — Security Vulnerability (Enterprise)

- **Both Agents:** Critical priority.  
- **Orchestrator:** Agrees, routes to Engineering.  
- **Final Decision:** `Technical - API`, `Critical`, `Engineering`

---

### Ticket ID: 1007 — Frontend Glitch (Premium)

- **Both Agents:** Medium priority, minor issue.  
- **Orchestrator:** Technical agent provides more specific categorization.  
- **Final Decision:** `Technical - Frontend/UI`, `Medium`, `DevOps`

---

## Known Limitations

### 1. No Ground Truth Accuracy
- **Issue:** No labeled dataset to validate correctness.
- **Impact:** Correctness score is only an approximation.

### 2. Limited Language Understanding
- **Issue:** Agents rely on keywords and basic rules.
- **Impact:** Cannot interpret nuanced language or intent.

### 3. Static Agent Execution
- **Issue:** All agents run on every ticket.
- **Impact:** Not optimized for performance or agent specialization.

### 4. Basic Conflict Resolution
- **Issue:** Orchestrator uses simple priority/max-value rules.
- **Impact:** May overlook more complex or context-sensitive factors.

### 5. No Confidence or Uncertainty Estimation
- **Issue:** Agents provide definitive outputs.
- **Impact:** Cannot flag low-confidence decisions for manual review.

### 6. No Learning or Feedback Loop
- **Issue:** Agents don’t learn from outcomes.
- **Impact:** System performance remains static over time.

### 7. No Real-Time System Integration
- **Issue:** Standalone simulation; no external APIs used.
- **Impact:** Not deployable in production without integration layers.

---

This evaluation framework provides a solid foundation to understand how the system behaves across typical scenarios and highlights the areas that can be improved for real-world deployment.The Output of all test cases and their evaluation metrics has been documented as comments in evaluation/test_cases.py .
