# Generated by Django 3.0.2 on 2020-01-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='061234567', max_length=50),
            preserve_default=False,
        ),
    ]
