# Generated by Django 3.2.15 on 2023-09-02 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=140, verbose_name='Фамилия и инициалы')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220, verbose_name='Название занятия')),
                ('group', models.CharField(blank=True, choices=[('23-PM-1', '23-ПМ-1'), ('23-PM-2', '23-ПМ-2')], default='23-PM-1', max_length=80, null=True, verbose_name='Название группы')),
                ('subgroup', models.CharField(blank=True, choices=[('Base-1', 'Подгруппа 1'), ('Base-2', 'Подгруппа 2'), ('Eng-1', 'Подгруппа 1 (англ)'), ('Eng-2', 'Подгруппа 2 (англ)')], default='Base-1', max_length=80, null=True, verbose_name='Название подгруппы')),
                ('lesson_type', models.CharField(blank=True, choices=[('Lecture', 'Лекция'), ('Practice', 'Практика'), ('Lab', 'Лаба')], default='Lecture', max_length=40, null=True, verbose_name='Тип занятия')),
                ('week_type', models.CharField(choices=[('Odd', 'Нечетная'), ('Even', 'Четная')], default='Odd', max_length=40, verbose_name='Тип недели')),
                ('lesson_date', models.CharField(choices=[('MON', 'Понедельник'), ('TUE', 'Вторник'), ('WED', 'Среда'), ('THU', 'Четверг'), ('FRI', 'Пятница'), ('SAT', 'Суббота'), ('SUN', 'Воскресенье')], default='SUN', max_length=40, verbose_name='День недели')),
                ('place', models.CharField(max_length=120, verbose_name='Место проведения')),
                ('time_start', models.TimeField(verbose_name='Время начала')),
                ('time_end', models.TimeField(verbose_name='Время завершения')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pm23.teacher', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Занятие',
                'verbose_name_plural': 'Занятия',
            },
        ),
    ]
