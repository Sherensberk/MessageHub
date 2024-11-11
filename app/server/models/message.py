from typing import Optional
from pydantic import BaseModel, Field

class MessageSchema(BaseModel):
    remetente: int = Field(...)
    destinatario: int = Field(...)
    conteudo: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "remetente": 12,
                "destinatario": 23,
                "conteudo": "Olá Henrycke",
            }
        }


class UpdateMessageModel(BaseModel):
    remetente: Optional[int]
    destinatario: Optional[int]
    conteudo: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "remetente": 23,
                "destinatario": 12,
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
