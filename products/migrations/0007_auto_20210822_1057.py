# Generated by Django 3.2.5 on 2021-08-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210822_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catears_has_colors',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='qupiu_custom_form',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
