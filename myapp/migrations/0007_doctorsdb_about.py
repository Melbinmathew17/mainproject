# Generated by Django 4.1.7 on 2023-07-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_service_db_delete_servicedb'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorsdb',
            name='About',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
