# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass # 추가로 필요한 필드가 있다면 여기에 작성하세요. 없다면 pass!