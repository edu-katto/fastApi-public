from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title = "My first API",
    description = "API creada para evaluar los conocimientos sobre FastApi",
    version = "1.0"
)

app.include_router(user)