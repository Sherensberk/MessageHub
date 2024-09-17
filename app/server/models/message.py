from typing import Optional
from pydantic import BaseModel, Field

class MessageSchema(BaseModel):
    remetente: str = Field(...)
    conteudo: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "remetente": "Cleber Souza",
                "conteudo": "Olá Henrycke",
            }
        }


class UpdateMessageModel(BaseModel):
    remetente: Optional[str]
    conteudo: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "remetente": "Cleber Souza",
                "conteudo": "Olá Henrycke",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
