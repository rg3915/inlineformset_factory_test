from django.contrib import admin
from .models import TaskAnswer, TaskAnswerFile


class TaskAnswerFileInline(admin.TabularInline):
    model = TaskAnswerFile
    extra = 0


@admin.register(TaskAnswer)
class TaskAnswerAdmin(admin.ModelAdmin):
    # list_display
    inlines = [TaskAnswerFileInline]
