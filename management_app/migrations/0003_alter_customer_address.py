# Generated by Django 4.0.3 on 2022-04-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_app', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(),
        ),
    ]
