import json

from channels.generic.websocket import AsyncWebsocketConsumer

from apps.chat.consumers.messages_operations import chat_message
from apps.chat.consumers.messages_operations import get_message
from apps.chat.consumers.messages_operations import mark_message_as_delivered
from apps.chat.consumers.messages_operations import mark_message_as_read
from apps.chat.consumers.messages_operations import message_deleted
from apps.chat.consumers.messages_operations import message_edited
from apps.chat.consumers.messages_operations import save_message
from apps.chat.consumers.messages_operations import send_last_messages
from apps.chat.consumers.messages_operations import serialize_message
from apps.chat.consumers.users_and_rooms_operations import authenticate_user
from apps.chat.consumers.users_and_rooms_operations import get_chat_room
from apps.chat.consumers.users_and_rooms_operations import get_recipient
from apps.chat.consumers.users_and_rooms_operations import is_user_in_chat
from apps.chat.consumers.users_and_rooms_operations import is_user_online
from apps.chat.consumers.users_and_rooms_operations import update_user_status


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.chat_group_name = f'chat_{self.room_id}'

        # Check if chat room exists
        self.room = await get_chat_room(self.room_id)
        if not self.room:
            return await self.close()

        # Authenticate user
        self.scope['user'] = await authenticate_user(self.scope)
        if not self.scope['user']:
            return await self.close()

        # Check if user is in chat
        if not await is_user_in_chat(self.room_id, self.scope['user'].email):
            return await self.close()

        # Connect to chat group
        await self.channel_layer.group_add(self.chat_group_name, self.channel_name)
        await self.accept()

        # Sending last messages
        await send_last_messages(self)

        # Update user status
        await update_user_status(self.scope['user'], is_online=True)

    async def disconnect(self, close_code):
        # Leave chat group
        await self.channel_layer.group_discard(self.chat_group_name, self.channel_name)

        # Update user status
        await update_user_status(self.scope['user'], is_online=False)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_text = data.get('message')
        if not message_text:
            return

        # Save message to database
        message = await save_message(self, message_text)

        # Send message to chat group
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message_id': message.id,
            },
        )

    async def chat_message(self, event):
        await chat_message(self, event)

    async def mark_message_as_delivered(self, message_id):
        await mark_message_as_delivered(self, message_id)

    async def mark_message_as_read(self, message_id):
        await mark_message_as_read(self, message_id)

    async def get_recipient(self):
        return await get_recipient(self.room, self.scope['user'])

    async def message_deleted(self, event):
        await message_deleted(self, event)

    async def message_edited(self, event):
        await message_edited(self, event)

    @staticmethod
    async def is_user_online(user):
        return await is_user_online(user)

    @staticmethod
    async def get_message(message_id):
        return await get_message(message_id)

    @staticmethod
    async def serialize_message(message):
        return await serialize_message(message)
