from django.urls import path

from secured_media.views import secured_file_view

app_name = "secured_media"

urlpatterns = [
    path("<token>", secured_file_view, name="secured_file"),
]
