from fastapi import APIRouter, Body, HTTPException

from server.interfaces.api import (
    get_user_messages,
)

from server.interfaces.users import *
from server.interfaces.messages import *
from server.models.response import *

router = APIRouter()

@router.get("/chat", response_description="Get messages and user info from another services and aggregate")
async def user_messages(user_id: str):
    return await get_user_messages(user_id)

user_router = APIRouter()

@user_router.post("/", response_model=ResponseModel, status_code=201)
async def add_user(user: dict = Body(...)):
    return await user_create(user)

@user_router.get("/{id}", response_model=Users)
async def get_user(id:str):
    return await user_get(id)

@user_router.put("/", response_model=ResponseModel)
async def update_user(user: dict = Body(...)):
    return await user_update(user)

@user_router.delete("/{id}", response_model=ResponseModel)
async def delete_user(id:str):
    return await user_delete(id)

message_router = APIRouter()

@message_router.post("/", response_description="Save Message")
async def add_message(message: dict = Body(...)):
    return await message_add(message)

@message_router.get("/{id}")
async def get_message(id:str):
    return await message_get(id)

@message_router.put("/{id}")
async def update_message(id, message: dict = Body(...)):
    return await message_update(id, message)

@message_router.delete("/{id}")
async def delete_message(id:str):
    return await message_delete(id)
