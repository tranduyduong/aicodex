from sqlalchemy import false

from users.repositories import UserRepository
from users.models import User
import re

class UserService:
    @staticmethod
    def get_all_users():
        return UserRepository.get_all()

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_by_id(user_id)

    @staticmethod
    def create_user(name, email):
        user = User(name=name, email=email)
        UserRepository.create(user)
        return user

    @staticmethod
    def update_user(user_id, name, email):
        user = UserRepository.get_by_id(user_id)
        if user:
            user.name = name
            user.email = email
            UserRepository.update()
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            UserRepository.delete(user)
            return True
        return False

    @staticmethod
    def get_user_by_email(email):
        # TODO Implementation here
        return False

    @staticmethod
    def is_valid_email(email):
        # Simple regex for email validation
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None