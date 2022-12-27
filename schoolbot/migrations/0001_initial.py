# Generated by Django 3.2.1 on 2022-12-21 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'ordering': ['grade'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('new', 'Новый'), ('done', 'Выполнен'), ('canceled', 'Отменен'), ('in_progress', 'В процессе')], default='new', max_length=255)),
                ('payment', models.CharField(choices=[('paid', 'Оплачен'), ('not_paid', 'Не оплачен')], default='not_paid', max_length=255)),
                ('photo', models.CharField(blank=True, max_length=500, null=True)),
                ('order', models.TextField(blank=True, null=True)),
                ('date_to_complete', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(unique=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_bot', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('bun', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('user', 'Пользователь'), ('student', 'Ученик'), ('teacher', 'Учитель')], default='user', max_length=255)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Пользователь Telegram',
                'verbose_name_plural': 'Пользователи Telegram',
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('teacher_comment', models.CharField(blank=True, max_length=300, null=True)),
                ('teacher_tasks_ban', models.BooleanField(default=False)),
                ('teach_tasks_paid', models.IntegerField(blank=True, null=True)),
                ('teach_tasks_not_paid', models.IntegerField(blank=True, null=True)),
                ('teach_tasks_solved', models.IntegerField(blank=True, null=True)),
                ('teach_tasks_pass', models.IntegerField(blank=True, null=True)),
                ('teach_tasks_not_solved_in_time', models.IntegerField(blank=True, null=True)),
                ('teach_tasks_arbitration', models.IntegerField(blank=True, null=True)),
                ('teach_tasks_arbitration_incorrect', models.IntegerField(blank=True, null=True)),
                ('tasks_arbitration_correctteach', models.IntegerField(blank=True, null=True)),
                ('teach_amount', models.IntegerField(blank=True, null=True)),
                ('teach_fee', models.IntegerField(blank=True, null=True)),
                ('teach_comission', models.IntegerField(blank=True, null=True)),
                ('teach_total_sum_to_pay', models.IntegerField(blank=True, null=True)),
                ('teach_paid', models.IntegerField(blank=True, null=True)),
                ('teach_level', models.IntegerField(default=1)),
                ('teach_calc_value', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='schoolbot.telegramuser')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, unique=True)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='schoolbot.grade')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['grade'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('stud_comment', models.CharField(blank=True, max_length=300, null=True)),
                ('stud_tasks_add', models.IntegerField(blank=True, null=True)),
                ('stud_tasks_paid', models.IntegerField(blank=True, null=True)),
                ('stud_tasks_pass', models.IntegerField(blank=True, null=True)),
                ('stud_tasks_solved', models.IntegerField(blank=True, null=True)),
                ('stud_tasks_not_paid', models.IntegerField(blank=True, null=True)),
                ('stud_tasks_ban', models.IntegerField(blank=True, null=True)),
                ('stud_tasks_arbitration', models.IntegerField(blank=True, null=True)),
                ('stud_tasks_arbitration_incorrect', models.IntegerField(blank=True, null=True)),
                ('tasks_arbitration_correctstud', models.IntegerField(blank=True, null=True)),
                ('stud_amount', models.IntegerField(blank=True, null=True)),
                ('stud_level', models.IntegerField(default=1)),
                ('stud_calc_value', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='schoolbot.telegramuser')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='OrderProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('done', 'Выполнен'), ('canceled', 'Отменен'), ('in_progress', 'В процессе'), ('dispute', 'Спор'), ('on_check', 'На проверке')], default='in_progress', max_length=255)),
                ('photo', models.CharField(blank=True, max_length=500, null=True)),
                ('doer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_doer', to='schoolbot.telegramuser')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_process', to='schoolbot.order')),
            ],
            options={
                'verbose_name': 'Процесс заказа',
                'verbose_name_plural': 'Процессы заказов',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='schoolbot.subject'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='schoolbot.telegramuser'),
        ),
    ]
