# Generated by Django 5.0.1 on 2024-01-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user12'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user12',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
