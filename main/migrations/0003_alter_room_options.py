# Generated by Django 4.2.4 on 2023-09-11 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
