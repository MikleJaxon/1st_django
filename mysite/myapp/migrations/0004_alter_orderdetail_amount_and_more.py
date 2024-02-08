# Generated by Django 5.0.1 on 2024-02-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='stripe_payment_intent',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
