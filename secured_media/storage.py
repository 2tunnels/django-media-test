from typing import Type
from urllib.parse import urlencode

from django.core.files.storage import FileSystemStorage
from django.db.models.base import ModelBase
from django.urls import reverse


class SecuredFileSystemStorage(FileSystemStorage):
    associated_model: Type[ModelBase]
    associated_field_name: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def url(self, name: str):
        return (
            reverse(
                "secured_media:secured_file", kwargs={"token": "super-secret-token"}
            )
            + "?"
            + urlencode(
                {
                    "name": name,
                    "associated_model": f"{self.associated_model.__module__}.{self.associated_model.__name__}",
                    "associated_field": self.associated_field_name,
                }
            )
        )
