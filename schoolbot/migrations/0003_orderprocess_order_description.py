# Generated by Django 3.2.1 on 2022-12-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolbot', '0002_orderprocess_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderprocess',
            name='order_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
