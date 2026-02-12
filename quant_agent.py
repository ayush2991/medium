from agents import Agent, Runner
import asyncio
import yfinance as yf
from agents import function_tool


@function_tool
def get_ticker_info(ticker: str) -> dict:
    """
    Fetches key financial and market information for a ticker.
    """
    stock = yf.Ticker(ticker)
    return stock.info


quant_agent = Agent(
    name="QuantAgent",
    model="gpt-5-nano",
    tools=[get_ticker_info],
    instructions="""
You are a quantitative equity analyst.
When given a stock ticker, provide a comprehensive analysis formatted in **clean Markdown** for rendering in a web UI.

Use the following structure:
1. **# [Ticker] Financial Outlook**: A high-level executive summary.
2. **## Key Strengths**: Bulleted list of positive catalysts and metrics.
3. **## Risks & Headwinds**: Bulleted list of potential downsides.
4. **## Portfolio Role**: How this asset fits into a diversified strategy.

**Formatting Guidelines:**
- Use bold text for key metrics.
- Use tables if comparing multiple data points.
- If data is unavailable, acknowledge the gap clearly.
- Clean up any special characters or formatting. Ensure the output is valid, simple markdown.
""",
)


async def get_analysis(ticker):
    result = await Runner.run(quant_agent, input=f"Provide an outlook for {ticker}")
    return result.final_output
