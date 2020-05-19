from django.shortcuts import render
import asyncio
import websockets


template = 'game/index.html'

async def startGame(websocket, path):
    move = await websocket.recv()
    await websocket.end("hello")
    



def game(request):
    start_server = websockets.serve(startGame, "127.0.0.1", 5678)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

    return render(request, template, {'range': range(9)})

# Web Sockets, Channels, AI Bot
