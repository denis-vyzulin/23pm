from django.contrib import admin
from .models import Teacher, Lesson


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'fullname',
    ]
    search_fields = [
        'fullname',
    ]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'group',
        'lesson_type',
        'week_type',
        'lesson_date',
    ]
    list_filter = [
        'group',
        'subgroup',
        'lesson_type',
        'week_type',
        'lesson_date',
    ]
    search_fields = [
        'name',
        'place',
        'teacher',
    ]
