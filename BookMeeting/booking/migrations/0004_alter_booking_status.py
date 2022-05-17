# Generated by Django 4.0.2 on 2022-03-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('booking', '0003_booking_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('-1', 'delete'), ('0', 'active'), ('1', 'completed')], default='0',
                                   max_length=20),
        ),
    ]
