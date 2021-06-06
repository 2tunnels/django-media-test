from typing import TYPE_CHECKING, Dict

from django.core.handlers.wsgi import WSGIRequest

from secured_media.fields import SecuredFileField

if TYPE_CHECKING:
    from service.apps.core.models import PrivateDocument, PrivatePhoto


class PrivateDocumentField(SecuredFileField):
    def has_permission(self, request: WSGIRequest, private_document: "PrivateDocument"):
        return request.user.is_superuser


class PrivatePhotoField(SecuredFileField):
    def has_permission(self, request: WSGIRequest, private_photo: "PrivatePhoto"):
        return request.user == private_photo.uploader
