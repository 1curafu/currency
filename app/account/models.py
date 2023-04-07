from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static


def avatar_path(instance, filename):
    return f"avatars/{instance.id}/{filename}"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.FileField(
        default=None,
        blank=True,
        null=True,
        upload_to=avatar_path
    )
    phone = models.CharField(
        max_length=64,
        unique=True,
        null=True,
        blank=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('anonym-avatar.png')
