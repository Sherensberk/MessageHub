from decouple import config
import requests
from server.models.response import *
from server.models.response import ResponseModel, ErrorResponseModel
SERVICE = config("USER_SERVICE")

async def user_get(id:str):
    response = requests.get(f"{SERVICE}/user_info", params={"id": id})
    response.raise_for_status()
    return Users(data=response.json())

async def user_create(data:dict):
    response = requests.post(f"{SERVICE}/user_create", json=data)
    response.raise_for_status()
    return ResponseModel(message=response._content)

async def user_update(data:dict):
    response = requests.put(f"{SERVICE}/user_update", json=data)
    response.raise_for_status()
    return ResponseModel(message=response._content)

async def user_delete(id:dict):
    response = requests.delete(f"{SERVICE}/user_info", params={"id": id})
    response.raise_for_status()
    return ResponseModel(message=response._content)