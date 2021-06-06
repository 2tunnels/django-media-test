from typing import Type

from django.core.files.storage import FileSystemStorage
from django.db.models.base import ModelBase
from django.urls import reverse

from secured_media.utils import encrypt_token


class SecuredFileSystemStorage(FileSystemStorage):
    associated_model: Type[ModelBase]
    associated_field_name: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def url(self, name: str):
        return reverse(
            "secured_media:secured_file",
            kwargs={
                "token": encrypt_token(
                    file_name=name,
                    associated_model=self.associated_model,
                    associated_field_name=self.associated_field_name,
                )
            },
        )
