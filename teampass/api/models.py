from django.db import models
from django.contrib.auth.models import User


class EncryptedItem(models.Model):
    data = models.TextField(
        verbose_name="Encrypted Data",
        name="Data"
    )

    data_type = models.IntegerField()


class ItemKey(models.Model):
    item = models.ForeignKey(
        EncryptedItem,
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    key = models.TextField(
        verbose_name="Item's key encrypted for the user",
        name="Item Key for User"
    )
