# Quant Agent: Design Doc

## 1. Goal
A modular, tool-augmented AI system for quantitative equity analysis. It combines LLM reasoning with external market data to provide grounded, data-driven insights.

## 2. Core Objectives
- **Data Grounding**: Use real-time data to prevent hallucinations.
- **Explainability**: Structured, data-backed reasoning.
- **Modularity**: Easy-to-add tools and agent roles.

## 3. Architecture
Built on the **OpenAI Agents SDK** using the Tool-Agent-Runner pattern.

### 3.1 Components
- **Tools**: `get_ticker_info` (wraps `yfiannce`) for financial metrics.
- **Agent**: `QuantAgent` (Analyst persona) running on `gpt-5-nano`.
- **Runner**: Manages the loop between user input, tool execution, and agent synthesis.

### 3.2 Data Flow
1. **Input**: User provides ticker (e.g., "NVDA").
2. **Retrieve**: Agent calls `yfinance` via tool for latest data.
3. **Analyze**: Agent processes metrics alongside internal knowledge.
4. **Report**: Markdown output covering Outlook, Strengths, Risks, and Portfolio Role.

## 4. Design Decisions
- **GPT-5 Nano**: Minimizes cost and latency for rapid prototyping.
- **yfinance**: Free, Pythonic, and no-auth. Ideal for MVP development.
- **OpenAI SDK**: Faster ramp-up and community support vs. enterprise SDKs.
- **Functional Tool Calling**: Enables reasoning over structured data rather than simple text retrieval (RAG).

## 5. Security & Limitations
- **Keys**: Managed via env variables.
- **Latency**: Data may be delayed; agent clarifies uncertainty.
- **Disclaimer**: For research purposes only; not licensed financial advice.

## 6. Future Roadmap
- **Memory**: Support for cross-ticker comparisons.
- **Multi-Agent**: Adding Portfolio Managers and Sector Analysts.
- **Human-in-the-loop**: Interactive research refinement.
