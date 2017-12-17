from django.db import models
from django.contrib.auth.models import User


class EncryptedItem(models.Model):
    """
    Some encrypted data. This will likely just be a blob of JSON,
    but the actual data time will be stored as an integer.
    Current data types:
    1. JSON user account in the style:
    {
        "site": "the website",
        "username": "the username",
        "password": "the password"
    }
    """
    data = models.TextField(
        verbose_name="Encrypted Data",
        name="Data"
    )

    data_type = models.IntegerField()


class ItemKey(models.Model):
    """
    The document key for an item, encrypted with a user's
    public key.
    """
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


class UserPublicKey(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    key = models.TextField()
