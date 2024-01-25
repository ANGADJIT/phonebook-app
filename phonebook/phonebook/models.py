from django.db import models
from uuid import uuid4
from uuid import UUID
from django.core.validators import RegexValidator


class Contact(models.Model):
    class ContactType(models.TextChoices):
        FAMILY = ('FAMILY', 'FAMILY')
        FRIENDS = ('FRIENDS', 'FRIENDS')
        WORK = ('WORK', 'WORK')

    id: UUID = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    phonenumber: models.CharField = models.CharField(
        validators=[RegexValidator(
            r'^[0-9]{10}$', 'Phone number should contain only numeric characters. or Numbers should be 10 digits')],
        unique=True,
        max_length=10
    )
    name: models.CharField = models.CharField(max_length=100)
    contact_type: models.CharField = models.CharField(
        max_length=7, choices=ContactType.choices)
