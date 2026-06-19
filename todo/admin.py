from django.contrib import admin
from todo.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Fields that will be displayed in the task list table
    list_display = ('content', 'created_at', 'deadline', 'is_done')

    # Fields by which you can filter tasks in the right panel
    list_filter = ('is_done', 'tags')

    # Fields by which the search will work
    # (the __ symbol means searching by
    # the name field of the associated Tag model)
    search_fields = ('content', 'tags__name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

    search_fields = ('name',)
