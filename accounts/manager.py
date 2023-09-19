from django.contrib.auth.models import BaseUserManager
from .models import User


class Mymanager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('please enter username')
        if not email:
            raise ValueError('please enter email')
        