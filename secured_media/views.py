from django.core.handlers.wsgi import WSGIRequest
from django.http import FileResponse, HttpResponseForbidden
from django.http.response import HttpResponseBase

from secured_media.utils import decrypt_token


def secured_file_view(request: WSGIRequest, token: str) -> HttpResponseBase:
    file_name, associated_model, associated_field_name = decrypt_token(token)

    # TODO: add check if record exits
    instance = associated_model.objects.get(**{associated_field_name: file_name})
    instance_field = getattr(instance, associated_field_name)

    if not instance_field.field.has_permission(request, instance):
        return HttpResponseForbidden()

    return FileResponse(open(instance_field.path, "rb"))
