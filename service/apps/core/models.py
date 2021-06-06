import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from service.apps.core.fields import PrivateDocumentField, PrivatePhotoField


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class PublicDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.FileField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)


class PrivateDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = PrivateDocumentField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)


class PrivatePhoto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = PrivatePhotoField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
