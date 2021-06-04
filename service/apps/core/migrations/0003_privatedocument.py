# Generated by Django 3.2.4 on 2021-06-04 21:39

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import secured_media.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_publicdocument"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrivateDocument",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("document", secured_media.fields.SecuredFileField(upload_to="")),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "uploader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]