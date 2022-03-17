# Generated by Django 3.2.6 on 2021-11-11 07:29

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20211111_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='join_ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=11, region=None),
        ),
    ]
