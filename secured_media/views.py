import importlib

from django.core.handlers.wsgi import WSGIRequest
from django.http import FileResponse


def secured_file_view(request: WSGIRequest, token: str) -> FileResponse:
    # TODO: get details from token, not query params
    name = request.GET["name"]
    associated_model = request.GET["associated_model"]
    associated_field = request.GET["associated_field"]

    module_name = _get_module_name_from_path(associated_model)
    class_name = _get_class_name_from_path(associated_model)

    module = importlib.import_module(module_name)
    cls = getattr(module, class_name)

    # TODO: add check if record exits
    instance = cls.objects.get(**{associated_field: name})

    filepath = getattr(instance, associated_field).path

    return FileResponse(open(filepath, "rb"))


def _get_module_name_from_path(path: str) -> str:
    return ".".join(path.split(".")[:-1])


def _get_class_name_from_path(path: str) -> str:
    return path.split(".")[-1]
