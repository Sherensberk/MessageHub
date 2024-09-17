import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.HUB
message_collection = database.get_collection("messages")

def message_helper(message) -> dict:
    return {
        "id": str(message["_id"]),
        "conteudo": message["conteudo"],
        "remetente": message["remetente"],
    }


# Retrieve all messages present in the database
async def retrieve_messages():
    messages = []
    async for message in message_collection.find():
        messages.append(message_helper(message))
    return messages


# Add a new message into to the database
async def add_message(message_data: dict) -> dict:
    message = await message_collection.insert_one(message_data)
    new_message = await message_collection.find_one({"_id": message.inserted_id})
    return message_helper(new_message)


# Retrieve a message with a matching ID
async def retrieve_message(id: str) -> dict:
    message = await message_collection.find_one({"_id": ObjectId(id)})
    if message:
        return message_helper(message)


# Update a message with a matching ID
async def update_message(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    message = await message_collection.find_one({"_id": ObjectId(id)})
    if message:
        updated_message = await message_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_message:
            return True
        return False


# Delete a message from the database
async def delete_message(id: str):
    message = await message_collection.find_one({"_id": ObjectId(id)})
    if message:
        await message_collection.delete_one({"_id": ObjectId(id)})
        return True
