# Generated by Django 3.2.5 on 2021-08-20 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_order_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatus',
            name='order_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.order'),
        ),
    ]