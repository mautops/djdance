# Generated by Django 4.2.13 on 2024-12-12 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("access", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="accesstoken",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="所有者",
            ),
        ),
    ]