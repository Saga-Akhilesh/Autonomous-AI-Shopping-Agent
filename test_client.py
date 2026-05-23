# import asyncio
# from fastmcp.client import Client
# from fastmcp.client.transports import StdioTransport

# async def main():
#     transport = StdioTransport(command="python", args=["mcp_server.py"])

#     async with Client(transport) as client:
#         print("\n🚀 AI Shopping Agent Started\n")
#         print(await client.call_tool("open_amazon"))
#         print(await client.call_tool("search_item", {"item": "chargers under 600"}))
#         print(await client.call_tool("open_first_prodauct"))
#         print(await client.call_tool("add_to_cart"))
#         print(await client.call_tool("checkout"))
#         print(await client.call_tool("payment"))
#         print(await client.call_tool("payment_cod_and_place", {"place": True}))

#         input("\nPress Enter to close browser...")

# asyncio.run(main())

import asyncio
from fastmcp.client import Client
from fastmcp.client.transports import StdioTransport

async def main():
    transport = StdioTransport(command="python", args=["mcp_server.py"])

    async with Client(transport) as client:
        print(await client.call_tool("buy", {"item": "charger under 600"}))

    input("Press Enter to close...")

asyncio.run(main())
