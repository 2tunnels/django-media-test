from django.db.models import FileField

from secured_media.storage import secured_storage


class SecuredFileField(FileField):
    def __init__(self, *args, **kwargs):
        kwargs.update({"storage": secured_storage})
        super().__init__(*args, **kwargs)
