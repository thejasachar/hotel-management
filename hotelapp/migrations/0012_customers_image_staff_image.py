# Generated by Django 5.0.1 on 2024-02-08 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0011_rename_guest_booking_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]