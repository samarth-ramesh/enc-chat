'Handles the websocket proto'

def handle_message(message: str) -> str:
    'handles a message'
    return message


async def handle(websocket):
    'handler middleware'
    async for message in websocket:
        websocket.send(handle(message))
