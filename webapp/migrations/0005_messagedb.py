# Generated by Django 4.1.7 on 2023-06-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_appoinmentdb_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='messagedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('message', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
