from urllib.parse import urlencode

from django.core.files.storage import FileSystemStorage
from django.urls import reverse


class SecuredFileSystemStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        self._associated_model = kwargs.pop("associated_model")
        self._associated_field = kwargs.pop("associated_field")

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
                    "associated_model": f"{self._associated_model.__module__}.{self._associated_model.__name__}",
                    "associated_field": self._associated_field,
                }
            )
        )
