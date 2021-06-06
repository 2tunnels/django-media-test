import importlib
import json
from typing import Tuple, Type

from cryptography.fernet import Fernet
from django.conf import settings
from django.db.models.base import ModelBase

_fernet = Fernet(settings.SECURED_MEDIA_SECRET_KEY.encode("utf-8"))


def encrypt_token(
    file_name: str, associated_model: Type[ModelBase], associated_field_name: str
) -> str:
    payload = json.dumps(
        {
            "file_name": file_name,
            "associated_model": f"{associated_model.__module__}.{associated_model.__name__}",
            "associated_field": associated_field_name,
        }
    )
    payload = payload.encode("utf-8")

    return _fernet.encrypt(payload).decode("utf-8")


def decrypt_token(token: str) -> Tuple[str, Type[ModelBase], str]:
    payload = _fernet.decrypt(token.encode("utf-8"))
    payload = payload.decode("utf-8")
    payload = json.loads(payload)

    module_name = _get_module_name_from_path(payload["associated_model"])
    class_name = _get_class_name_from_path(payload["associated_model"])

    module = importlib.import_module(module_name)
    cls = getattr(module, class_name)

    return payload["file_name"], cls, payload["associated_field"]


def extract_timestamp_from_token(token: str) -> int:
    return _fernet.extract_timestamp(token.encode("utf-8"))


def _get_module_name_from_path(path: str) -> str:
    return ".".join(path.split(".")[:-1])


def _get_class_name_from_path(path: str) -> str:
    return path.split(".")[-1]
