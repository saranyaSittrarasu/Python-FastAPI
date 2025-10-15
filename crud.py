from fastapi import  APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
def add(a: int, b: int):
    return a + b

class CrudModel(BaseModel):
    a: int
    b: int

@router.post("/subtract")
def subtract(model: CrudModel):
    return model.a - model.b

@router.post("/multiply")
def multiply(model: CrudModel):
    return model.a * model.b

@router.post("/divide")
def divide(model: CrudModel):
    if model.b == 0:
        return {"error": "Division by zero is not allowed."}
    return model.a / model.b
