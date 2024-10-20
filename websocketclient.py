import asyncio
import websockets

# Client function to connect to the WebSocket server and send messages
async def send_messages():
    url = "ws://localhost:8765"
    
    async with websockets.connect(url) as websocket:
        for i in range(10000):  # Run 10,000 times
            message = f"Request [{i}]"
            # Send message to the server
            await websocket.send(message)
            print(f"Sent: {message}")
            
            # Receive the modified message from the server
            response = await websocket.recv()
            print(f"Received: {response}")

# Main function to run the WebSocket client
if __name__ == "__main__":
    asyncio.run(send_messages())

