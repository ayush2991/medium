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
When given a stock ticker:
- Provide a structured outlook.
- Include areas of strength.
- Include key risks.
- Describe what role this stock might play in a diversified portfolio.
- If you do not have current data, acknowledge uncertainty.
""",
)


async def get_analysis(ticker):
    result = await Runner.run(quant_agent, input=f"Provide an outlook for {ticker}")
    return result.final_output
