# Generated by Django 5.1.4 on 2024-12-23 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите телеграмм chat-id",
                max_length=50,
                null=True,
                verbose_name="Телеграмм chat-id",
            ),
        ),
    ]
