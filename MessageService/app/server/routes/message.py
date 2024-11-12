from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_message,
    delete_message,
    retrieve_message,
    retrieve_messages,
    update_message,
)
from server.models.message import (
    ErrorResponseModel,
    ResponseModel,
    MessageSchema,
    UpdateMessageModel,
)

from server.bus import ServiceBusManager

bus = ServiceBusManager()
router = APIRouter()


@router.post("/", response_description="Message data added into the database")
async def add_message_data(message: MessageSchema = Body(...)):
    message = jsonable_encoder(message)
    bus.send_message({'id':message['remetente']})
    new_message = await add_message(message)
    return ResponseModel(new_message, "Message added successfully.")


@router.get("/{id}", response_description="Messages retrieved")
async def get_messages(id):
    messages = await retrieve_messages(id)
    if messages:
        return ResponseModel(messages, "Messages data retrieved successfully")
    return ResponseModel(messages, "Empty list returned")


@router.get("/{id}", response_description="Message data retrieved")
async def get_message_data(id):
    message = await retrieve_message(id)
    if message:
        return ResponseModel(message, "Message data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Message doesn't exist.")


@router.put("/{id}")
async def update_message_data(id: str, req: UpdateMessageModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_message = await update_message(id, req)
    if updated_message:
        return ResponseModel(
            "Message with ID: {} name update is successful".format(id),
            "Message name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the message data.",
    )


@router.delete("/{id}", response_description="Message data deleted from the database")
async def delete_message_data(id: str):
    deleted_message = await delete_message(id)
    if deleted_message:
        return ResponseModel(
            "Message with ID: {} removed".format(id), "Message deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Message with id {0} doesn't exist".format(id)
    )
