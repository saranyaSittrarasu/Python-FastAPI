from fastapi import FastAPI
from crud import router as crud_router
from calculator import router as calculator_router

app = FastAPI()

app.include_router(crud_router)
app.include_router(calculator_router)