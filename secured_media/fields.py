from typing import Any, Type

from django.conf import settings
from django.db.models import FileField
from django.db.models.base import ModelBase

from secured_media.storage import SecuredFileSystemStorage


class SecuredFileField(FileField):
    def contribute_to_class(
        self, cls: Type[ModelBase], name: str, **kwargs: Any
    ) -> None:
        self.storage = SecuredFileSystemStorage(
            associated_model=cls,
            associated_field=name,
            location=settings.SECURED_MEDIA_ROOT,
        )
        super().contribute_to_class(cls, name, **kwargs)
