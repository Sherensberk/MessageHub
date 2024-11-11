from server.interfaces.messages import (
    message_history_get
)
from server.interfaces.users import (
    user_get
)

async def get_user_messages(user_id: str):
    messages = await message_history_get(user_id)
    user_info = await user_get(user_id)

    return {
        "user_name": user_info.data[0].nickname,  # Adjust based on the actual structure of user info response
        "messages": messages["data"]
    }