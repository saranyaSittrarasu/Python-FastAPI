from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class CalculatorModel(BaseModel):
    a: int
    b: int
    operation: str


@router.post("/calculator")
def calculator(model: CalculatorModel):
    if model.operation == "add":
        return model.a + model.b
    elif model.operation == "subtract":
        return model.a - model.b
    elif model.operation == "multiply":
        return model.a * model.b
    elif model.operation == "divide":
        if model.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        return model.a / model.b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Supported operations are add, subtract, multiply, divide.")

