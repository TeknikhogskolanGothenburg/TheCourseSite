import datetime

from bson import ObjectId
from flask_login import current_user

from app.controllers.user_controller import get_user_by_full_name
from app.persitence.repository import message_repository
from app.persitence.repository.user_repository import get_user_by_id


def create_message(to, message):
    recipient = get_user_by_full_name(to)
    message_dict = {
        'receiver': recipient._id,
        'sender': current_user._id,
        'message_body': message,
        'sent': datetime.datetime.now(),
        'read': False
    }
    message_repository.create_message(message_dict)


def get_all_messages_for_user():
    messages = message_repository.get_all_messages_for_user(current_user._id)
    for message in messages:
        message.sender = get_user_by_id(message.sender)
        message.receiver = current_user

    return messages


def get_message_by_id(message_id):
    return message_repository.get_message_by_id(message_id)


def get_new_msg_count_for_user(user_id):
    user_id = ObjectId(user_id)
    return message_repository.get_unread_msg_count(user_id)
