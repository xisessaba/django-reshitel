# Generated by Django 3.2.1 on 2022-12-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderprocess',
            name='payment',
            field=models.CharField(choices=[('paid', 'Оплачен'), ('not_paid', 'Не оплачен')], default='not_paid', max_length=255),
        ),
    ]
