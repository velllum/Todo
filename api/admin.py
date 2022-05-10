from django.contrib import admin

from . import models


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'slug', 'description', 'content', 'created_date', 'updated_date', 'is_relevant', 'is_public', 'author',
        'status'
    ]
    list_filter = ['author', 'status', 'is_public', 'is_relevant']
    search_fields = [
        'title', 'slug', 'description', 'content', 'created_date', 'updated_date', 'is_relevant', 'is_public', 'author',
        'status'
    ]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'note', 'user', 'created_date']
    list_filter = ['note', 'user', 'created_date']
    search_fields = ['user__get_full_name', 'note__title', 'text']


@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date']
    list_display_links = ['name']
    list_filter = ['created_date', 'updated_date']
    search_fields = ['name']
