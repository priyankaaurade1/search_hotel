# Generated by Django 3.2.11 on 2022-10-03 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='hotelimage',
            name='hotel',
        ),
        migrations.DeleteModel(
            name='Amenities',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='HotelImage',
        ),
    ]
