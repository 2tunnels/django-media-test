from abc import ABC, abstractmethod
from typing import Any, Dict, Type

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import FileField
from django.db.models.base import ModelBase

from secured_media.storage import SecuredFileSystemStorage


class SecuredFileField(ABC, FileField):
    storage: SecuredFileSystemStorage

    def __init__(self, *args, **kwargs):
        kwargs["unique"] = True
        kwargs["storage"] = SecuredFileSystemStorage(
            location=settings.SECURED_MEDIA_ROOT,
        )
        super().__init__(*args, **kwargs)

    def contribute_to_class(
        self, cls: Type[ModelBase], name: str, **kwargs: Any
    ) -> None:
        self.storage.associated_model = cls
        self.storage.associated_field_name = name
        super().contribute_to_class(cls, name, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["unique"]
        del kwargs["storage"]
        return name, path, args, kwargs

    @abstractmethod
    def has_permission(self, request: WSGIRequest, instance: ModelBase):
        pass

    def get_headers(self, request: WSGIRequest) -> Dict[str, str]:
        return {}
