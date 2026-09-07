# Real-Time Chat App

A real-time chat app I built during my backend engineering internship at Zare Innovation.

Users join a room by name and chat live with anyone else in the same room. Messages are saved to a database so when you join a room you can see what was said before you arrived. Each message shows who sent it.

## Stack
Python, FastAPI, WebSockets, SQLAlchemy, SQLite, bcrypt

## Run it

git clone https://github.com/yafetgurji24-collab/RealTimeChatApp.git
cd RealTimeChatApp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

Then open `test.html` in your browser to use the chat.

## Endpoints
- POST `/signup` — create account
- POST `/login` — get JWT token
- WebSocket `/ws/{room_id}?email={username}` — join a room and chat
