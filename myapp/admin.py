from django.contrib import admin
from .models import Task, SubTask, Category

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'categories')
        }),
        ('Task Details', {
            'fields': ('status', 'deadline'),
            'description': 'Статус и дедлайн задачи'
        }),
    )

class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'deadline', 'created_at')
    list_filter = ('status', 'task__title')  # Filter by task title
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'task')
        }),
        ('SubTask Details', {
            'fields': ('status', 'deadline'),
            'description': 'Статус и дедлайн подзадачи'
        }),
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)
admin.site.register(Category, CategoryAdmin)
