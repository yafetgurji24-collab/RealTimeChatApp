from User.routes import router
from Message.routes import routers
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
app.include_router(routers)