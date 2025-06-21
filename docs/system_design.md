# System Architecture

## Why Use Multiple Agents?

Instead of relying on a single, general-purpose AI model, this system adopts a **multi-agent architecture** to handle support tickets. The key idea is to divide the problem into specialized tasks, each handled by a dedicated expert.

### Meet the Agents

#### TechnicalAnalyzerAgent

Focuses on the **"what"** — the technical problem described in the ticket. It scans for error codes, system-related phrases, broken features, and other technical patterns using keyword matching.

#### CustomerContextAgent

Focuses on the **"who"** — the customer profile behind the ticket. It considers customer tier, revenue, and interaction history to evaluate urgency from a business impact perspective.

---

## Why This Approach Works

### Higher Accuracy

Each agent focuses on a narrow and well-defined aspect of the problem, enabling more accurate assessments and minimizing noise.

### Modular by Design

Agents are fully decoupled. You can update, retrain, or replace one agent without affecting others. For example, adding a new agent like `SentimentAnalyzer` is straightforward.

### Scalable

The architecture supports future growth. New agents can be introduced to handle additional ticket dimensions (e.g., compliance checks, regional routing) without redesigning the system.

### Resilient

Agents complement each other. If one agent misses a cue, another might catch it. The orchestrator coordinates their outputs to ensure critical information is not lost.

### Transparent and Explainable

Instead of a black-box output, the system offers layered reasoning. For example:

> "The technical agent identified this as a backend error, while the customer agent elevated the priority due to enterprise status."

---

## Design Decisions and Rationale

### 1. Pydantic for Structured Data

- **Decision:**  
  Use Pydantic to define the core data models (`Ticket`, `AgentOutput`).

- **Rationale:**  
  Pydantic enforces strict validation and type safety, ensuring clean and consistent data exchange across the system. It reduces runtime errors and supports maintainable code through clear data contracts.

---

### 2. Specialized Agents

- **Decision:**  
  Implement two agents: `TechnicalAnalyzerAgent` and `CustomerContextAgent`.

- **Rationale:**  
  Each support ticket involves two primary dimensions:
  
  - What is the issue? (Technical scope)  
  - Who is facing it? (Customer value and relationship)

  Assigning each concern to a focused agent enhances clarity, reduces complexity, and enables more meaningful decision-making.

---

### 3. Central Orchestrator

- **Decision:**  
  The `process_ticket()` function in `main.py` acts as the orchestrator.

- **Responsibilities:**
  - Delegates the ticket to each agent
  - Collects and aggregates the agent outputs
  - Resolves conflicts in priority or category
  - Produces a unified decision and reasoning explanation

- **Example:**  
  If the technical agent assigns "Medium" priority but the customer agent suggests "High" (e.g., enterprise client), the orchestrator escalates to "High" to ensure timely response.  
  Routing logic is also handled intelligently:  
  - Technical issues go to Engineering  
  - Access or relationship issues go to Customer Success

---

### 4. Heuristic-Based Agent Logic

- **Decision:**  
  Agents use rule-based logic (e.g., `if-else` conditions and keyword matching).

- **Rationale:**  
  The focus of this project is to demonstrate multi-agent collaboration and orchestrated decision-making, not to showcase advanced AI models.  
  Rule-based logic offers transparency, ease of debugging, and full control.  
  This setup also serves as a foundation where agents can later be upgraded with ML/LLM models while retaining the same structural backbone provided by Pydantic.

---

This modular architecture strikes a balance between simplicity, clarity, and future extensibility—ideal for demonstrating the power of collaborative, specialized agents in AI system design.
