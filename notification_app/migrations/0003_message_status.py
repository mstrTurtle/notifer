# Generated by Django 4.2.4 on 2023-08-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notification_app", "0002_message_email_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="status",
            field=models.TextField(default="idle"),
            preserve_default=False,
        ),
    ]
