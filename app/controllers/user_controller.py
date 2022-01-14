import datetime

from werkzeug.security import generate_password_hash
from app.persitence.repository import user_repository


def create_user(first_name, last_name, email, password):
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'full_name': f'{first_name} {last_name}',
        'email': email,
        'password': generate_password_hash(password),
        'admin': False,
        'instructor': False,
        'date_created': datetime.datetime.now(),
        'last_signin': None,
        'status': 'offline',
        'activated': False,
        'avatar': f'https://eu.ui-avatars.com/api/?name={first_name}+{last_name}&background=random',
        'address': {
            'address_line_1': None,
            'address_line_2': None,
            'zip': None,
            'state': None,
            'country': None
        },

        'courses': [],
        'settings': None,
        'social_profiles': None
    }

    user_repository.create_user(user)