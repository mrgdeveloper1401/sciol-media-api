from typing import Any
from django.contrib.auth.models import UserManager


class UserManagers(UserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('please enter email address')
        if not username:
            raise ValueError('please enter username')
        
        user = self.model(
            email=email,
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # def create_superuser(self, username: str, email: str | None, password: str | None):
    #     user = self.create_user(
    #         email=email,
    #         username=username,
    #         password=password
    #     )
    #     user.is_staff = True
    #     user.is_superuser = True
    #     user.save(using=self._db)
    #     return user
        