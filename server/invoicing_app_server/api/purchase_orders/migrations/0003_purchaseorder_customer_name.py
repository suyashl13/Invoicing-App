# Generated by Django 4.0.1 on 2022-01-13 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0002_purchaseorder_is_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='customer_name',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
    ]