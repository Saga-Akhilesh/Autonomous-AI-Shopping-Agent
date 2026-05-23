import streamlit as st
import asyncio
from fastmcp.client import Client
from fastmcp.client.transports import StdioTransport

st.set_page_config(page_title="AI Shopping Agent", layout="centered")

st.title("🛒 Autonomous AI Shopping Agent")

query = st.text_input("Enter product to buy")

mode = st.selectbox(
    "Select strategy",
    ["cheap", "best"],
    index=0
)

buy_btn = st.button("🚀 Start Autonomous Shopping")

if buy_btn and query:

    st.info("Agent started... watch browser 👀")

    async def run_agent():
        transport = StdioTransport(
            command="python",
            args=["mcp_server.py"]
        )

        async with Client(transport) as client:
            res = await client.call_tool(
                "buy",
                {
                    "item": query,
                    "mode": mode
                }
            )
            return res

    result = asyncio.run(run_agent())

    st.success("Agent finished")
    st.write(result)
