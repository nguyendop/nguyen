# Generated by Django 4.0.2 on 2022-03-17 06:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('booking', '0003_booking_room'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-time_from']},
        ),
    ]
