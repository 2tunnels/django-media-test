from django.core.handlers.wsgi import WSGIRequest
from django.http import FileResponse, HttpResponseForbidden
from django.http.response import HttpResponseBase
from django.shortcuts import get_object_or_404

from secured_media.fields import SecuredFileField
from secured_media.utils import decrypt_token


def secured_file_view(request: WSGIRequest, token: str) -> HttpResponseBase:
    file_name, associated_model, associated_field_name = decrypt_token(token)

    field: SecuredFileField = getattr(associated_model, associated_field_name).field

    instance = get_object_or_404(associated_model, **{associated_field_name: file_name})

    if not field.has_permission(request, instance):
        return HttpResponseForbidden()

    field_value = getattr(instance, associated_field_name)

    return FileResponse(
        open(field_value.path, "rb"), headers=field.get_headers(request)
    )
