# Generated by Django 3.2.1 on 2022-12-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolbot', '0003_orderprocess_order_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='photo',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
    ]
