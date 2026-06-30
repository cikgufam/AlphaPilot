from fastapi import FastAPI

from app.routes import home, health

app = FastAPI(title="AlphaPilot")

app.include_router(home.router)
app.include_router(health.router)