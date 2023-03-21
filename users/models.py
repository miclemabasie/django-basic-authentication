from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(verbose_name=_("Location"), max_length=255)

    def __str__(self):
        return f"{self.user.username}'s Profile"
