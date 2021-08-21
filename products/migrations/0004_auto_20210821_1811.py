# Generated by Django 3.2.5 on 2021-08-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210821_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catearcolor',
            name='name',
        ),
        migrations.AddField(
            model_name='catearcolor',
            name='catear_color',
            field=models.CharField(choices=[('BL', 'blue'), ('PN', 'pink'), ('GR', 'green'), ('WH', 'white'), ('BK', 'black')], default='BL', max_length=2),
        ),
    ]
