from django.contrib import admin

from service.apps.core.models import PrivateDocument, PublicDocument, User


class CustomUserAdmin(admin.ModelAdmin):
    pass


class PublicDocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "document", "uploader")


class PrivateDocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "document", "uploader")


admin.site.register(User, CustomUserAdmin)
admin.site.register(PublicDocument, PublicDocumentAdmin)
admin.site.register(PrivateDocument, PrivateDocumentAdmin)
