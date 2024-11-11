from pydantic import BaseModel, Field
from typing import List, Optional

class User(BaseModel):
    id: Optional[int]
    nickname: str = Field(...)
    email: str = Field(...)

class Users(BaseModel):
    data: List[User]

class Message(BaseModel):
    remetente: str = Field(...)
    conteudo: str = Field(...)

class Messages(BaseModel):
    messages: List[Message]

class ResponseModel(BaseModel):
   message: Optional[str]


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
