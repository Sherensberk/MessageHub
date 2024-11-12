from decouple import config
import requests

SERVICE = config("MESSAGE_SERVICE")

# get all messages present in the database
async def message_history_get(id:str) -> dict:
    messages_response = requests.get(f"{SERVICE}/message/{id}")
    messages_response.raise_for_status()
    return messages_response.json()

# Add a new message into to the database
async def message_add(message_data: dict) -> dict:
    messages_response = requests.post(f"{SERVICE}/message", json=message_data)
    messages_response.raise_for_status()
    return messages_response.json()

# get a message with a matching ID
async def message_get(id: str) -> dict:
    messages_response = requests.get(f"{SERVICE}/message/{id}")
    messages_response.raise_for_status()
    return messages_response.json()

# Update a message with a matching ID
async def message_update(id: str, data: dict) -> dict:
    messages_response = requests.put(f"{SERVICE}/message/{id}", json=data)
    messages_response.raise_for_status()
    return messages_response.json()

# Delete a message from the database
async def message_delete(id: str) -> dict:
    messages_response = requests.delete(f"{SERVICE}/message/{id}")
    messages_response.raise_for_status()
    return messages_response.json()