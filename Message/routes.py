from fastapi import APIRouter, WebSocket
from database import sessionMaker
from Message.models import MessageDB
from datetime import datetime

routers = APIRouter()

rooms={}

@routers.websocket("/ws/{roomId}")
async def websocketEndpoint(websocket:WebSocket, roomId:str):
    await websocket.accept()
    if roomId not in rooms:
        rooms[roomId] = []
    rooms[roomId].append(websocket)
    messages = []
    db = sessionMaker()
    messages = db.query(MessageDB).filter(MessageDB.roomId == roomId).all()
    for history in messages:
        await websocket.send_text(history.content)

    try:
        while True:
            message = await websocket.receive_text()
            db = sessionMaker()
            newMessage = MessageDB(roomId = roomId, content = message, timestamp = datetime.now())
            db.add(newMessage)
            db.commit()
            db.close()
            for connection in rooms[roomId]:
                await connection.send_text(message)

    except Exception:
        rooms[roomId].remove(websocket)


