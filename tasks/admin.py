from django.contrib import admin
from .models import SimpleTask

@admin.register(SimpleTask)
class SimpleTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'user')
    list_filter = ('completed', 'user', 'due_date', 'priority')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at',)
