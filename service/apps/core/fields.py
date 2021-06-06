from typing import TYPE_CHECKING

from django.core.handlers.wsgi import WSGIRequest

from secured_media.fields import SecuredFileField

if TYPE_CHECKING:
    from service.apps.core.models import PrivateDocument


class PrivateDocumentField(SecuredFileField):
    def has_permission(self, request: WSGIRequest, private_document: "PrivateDocument"):
        return request.user == private_document.uploader or request.user.is_superuser
