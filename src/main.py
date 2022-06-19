import asyncio
import imp
from websockets import serve
from server import handle

async def main():
    async with serve(serve, handle, 8765):
        await asyncio.Future()

asyncio.run(main())