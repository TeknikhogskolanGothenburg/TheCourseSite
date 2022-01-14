from app.persitence.models import User


def create_user(user):
    User(user).save()
