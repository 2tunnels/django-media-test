from django.contrib import admin

from service.apps.core.models import PublicDocument, User


class CustomUserAdmin(admin.ModelAdmin):
    pass


class PublicDocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "document", "uploader")


admin.site.register(User, CustomUserAdmin)
admin.site.register(PublicDocument, PublicDocumentAdmin)
