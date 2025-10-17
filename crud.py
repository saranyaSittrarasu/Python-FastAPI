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


user_db={1:{"name":"Saran","age":30},2:{"name":"Aeira","age":25},3:{"name":"Achu","age":22}}

class UserModel(BaseModel):
    name: str
    age: int

@router.put("/users/{user_id}")
def update_user(user_id: int, user: UserModel):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return {"message": "User updated successfully", "user": user_db[user_id]}
    return {"error": "User not found"}


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        print(user_db)
        return {"message": "User deleted successfully"}
    return {"error": "User not found"}