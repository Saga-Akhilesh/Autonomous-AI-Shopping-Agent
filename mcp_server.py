from fastmcp import FastMCP
from amazon_tools import get_bot
import asyncio

mcp = FastMCP("amazon-agent")
bot = get_bot()


@mcp.tool()
async def open_amazon():
    return await bot.open_amazon()

@mcp.tool()
async def search_item(item: str):
    return await bot.search_item(item)

@mcp.tool()
async def open_first_product():
    return await bot.open_first_product()

@mcp.tool()
async def add_to_cart():
    return await bot.add_to_cart()

@mcp.tool()
async def checkout():
    return await bot.go_to_checkout()

@mcp.tool()
async def payment():
    return await bot.go_to_payment()

@mcp.tool()
async def payment_cod_and_place(place: bool = False):
    return await bot.payment_cod_and_place(place)


# 🔥 NEW AUTONOMOUS TOOL
@mcp.tool()
async def buy(item: str):
    return await bot.autonomous_buy(item)
from fastmcp import FastMCP
from amazon_tools import get_bot
import asyncio

mcp = FastMCP("amazon-agent")
bot = get_bot()

@mcp.tool()
async def buy(item: str, mode: str = "cheap"):
    return await bot.autonomous_buy(item, mode)




if __name__ == "__main__":
    asyncio.run(mcp.run_async())
