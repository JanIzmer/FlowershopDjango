# Generated by Django 5.0.4 on 2025-04-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'W oczekiwaniu'), ('in_delivery', 'W dostawie'), ('completed', 'Dostarczone'), ('cancelled', 'Anulowane')], default=('in_delivery', 'W dostawie'), max_length=50),
        ),
    ]
