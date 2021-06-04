from django.conf import settings
from django.core.files.storage import FileSystemStorage

secured_storage = FileSystemStorage(
    location=settings.SECURED_MEDIA_ROOT, base_url=settings.SECURED_MEDIA_URL
)
