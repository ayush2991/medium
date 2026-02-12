# 📈 Quant Agent

An AI-powered quantitative equity analyst that leverages the **OpenAI Agents SDK** and **yfinance** to provide real-time financial insights.

## 🚀 Overview

Quant Agent acts as a virtual research assistant. By simply entering a stock ticker, the agent fetches the latest market data and synthesizes a comprehensive outlook, highlighting strengths, risks, and its potential role in a diversified portfolio.

## 🛠️ Setup

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repo-url>
   cd quant-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   *Note: For Streamlit Cloud deployment, add `OPENAI_API_KEY` to your secrets.*

## 💻 Usage

### Streamlit Web Interface (Recommended)
Launch the interactive dashboard:
```bash
streamlit run app.py
```

### CLI Analysis
You can also call the analysis function programmatically or import it into your own scripts:
```python
from quant_agent import get_analysis
import asyncio

async def main():
    print(await get_analysis("AAPL"))

if __name__ == "__main__":
    asyncio.run(main())
```

## 📁 Project Structure

- `app.py`: Streamlit-based web dashboard.
- `quant_agent.py`: Core logic for the AI analyst and data tools.
- `DESIGN.md`: Detailed system architecture and design justifications.
- `requirements.txt`: Python package dependencies.

---
*Disclaimer: This tool is for research purposes only and does not constitute financial advice.*
