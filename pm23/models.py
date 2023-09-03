from django.db import models


class Teacher(models.Model):
    fullname = models.CharField(max_length=140, verbose_name='Фамилия и инициалы')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.fullname


class Lesson(models.Model):
    GROUPS = (
        ('23-PM-1', '23-ПМ-1'),
        ('23-PM-2', '23-ПМ-2'),
    )
    SUBGROUPS = (
        ('Base-1', 'Подгруппа 1'),
        ('Base-2', 'Подгруппа 2'),
        ('Eng-1', 'Подгруппа 1, англ'),
        ('Eng-2', 'Подгруппа 2, англ'),
    )
    LESSON_TYPES = (
        ('Lecture', 'лекция'),
        ('Practice', 'практика'),
        ('Lab', 'лабораторная')
    )
    WEEK_TYPES = (
        ('Odd', 'Нечетная'),
        ('Even', 'Четная'),
    )
    LIST_OF_DAYS = (
        ('MON', 'Понедельник'),
        ('TUE', 'Вторник'),
        ('WED', 'Среда'),
        ('THU', 'Четверг'),
        ('FRI', 'Пятница'),
        ('SAT', 'Суббота'),
        ('SUN', 'Воскресенье'),
    )
    name = models.CharField(max_length=220, verbose_name='Название занятия')
    group = models.CharField(choices=GROUPS, default='23-PM-1', max_length=80,
                             verbose_name='Название группы', null=True, blank=True)
    subgroup = models.CharField(choices=SUBGROUPS, default='Base-1', max_length=80,
                                verbose_name='Название подгруппы', null=True, blank=True)
    lesson_type = models.CharField(choices=LESSON_TYPES, default='Lecture', max_length=40,
                                   verbose_name='Тип занятия', null=True, blank=True)
    week_type = models.CharField(choices=WEEK_TYPES, default='Odd', max_length=40,
                                 verbose_name='Тип недели', null=True, blank=True)
    lesson_date = models.CharField(choices=LIST_OF_DAYS, default='SUN', max_length=40,
                                   verbose_name='День недели')
    place = models.CharField(max_length=120, verbose_name='Место проведения')
    time_start = models.TimeField(verbose_name='Время начала')
    time_end = models.TimeField(verbose_name='Время завершения')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True,
                                blank=True, verbose_name='Преподаватель')
    
    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
    
    def __str__(self):
        return self.name
