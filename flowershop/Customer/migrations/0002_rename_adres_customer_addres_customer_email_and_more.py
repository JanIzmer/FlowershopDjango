# Generated by Django 5.0.4 on 2025-04-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='adres',
            new_name='addres',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='firstname',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='secondname',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
