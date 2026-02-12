# Quant Agent: Design Doc

## 1. Goal
A modular, tool-augmented AI system for quantitative equity analysis. It combines LLM reasoning with external market data to provide grounded, data-driven insights through an accessible web interface.

## 2. Core Objectives
- **Data Grounding**: Use real-time data to prevent hallucinations.
- **Explainability**: Structured, data-backed reasoning.
- **Modularity**: Easy-to-add tools and agent roles.
- **Accessibility**: A simple Streamlit UI for non-technical users.

## 3. Architecture
The system follows a multi-layered approach:
1. **Frontend**: Streamlit-based web app.
2. **Agent Layer**: OpenAI Agents SDK managing the interaction.
3. **Tool Layer**: Python functions interfacing with external APIs.

### 3.1 Components
- **Web UI (`app.py`)**: Built with **Streamlit**. Handles user input and displays markdown responses.
- **Agent (`quant_agent.py`)**: `QuantAgent` (Analyst persona) running on `gpt-5-nano`.
- **Tools**: `get_ticker_info` (wraps `yfinance`) for financial metrics.
- **Runner**: Manages the loop between user input, tool execution, and agent synthesis.

### 3.2 Data Flow
1. **Input**: User enters a ticker (e.g., "NVDA") in the Streamlit text box.
2. **Trigger**: User clicks "Run", initiating an `async` call to the agent runner.
3. **Retrieve**: Agent identifies the need for data and calls `yfinance` via the `get_ticker_info` tool.
4. **Analyze**: Agent processes metrics alongside internal knowledge.
5. **Synthesis**: Agent generates a structured report.
6. **Output**: Streamlit renders the Markdown response to the UI.

## 4. Design Decisions
- **GPT-5 Nano**: Minimizes cost and latency for rapid prototyping.
- **yfinance**: Free, Pythonic, and no-auth. Ideal for MVP development.
- **OpenAI SDK**: Faster ramp-up and community support vs. enterprise SDKs.
- **Streamlit**: Enables rapid deployment of a professional-looking web UI without complex frontend development.
- **Functional Tool Calling**: Enables reasoning over structured data rather than simple text retrieval (RAG).

## 5. Security & Limitations
- **Keys**: Managed via env variables locally and Streamlit Secrets in production.
- **Latency**: Data may be delayed; agent clarifies uncertainty.
- **Disclaimer**: For research purposes only; not licensed financial advice.

## 6. Future Roadmap
- **Memory**: Support for cross-ticker comparisons.
- **Multi-Agent**: Adding Portfolio Managers and Sector Analysts.
- **Charts**: Integration of interactive Plotly charts in the Streamlit UI.
- **Human-in-the-loop**: Interactive research refinement.
