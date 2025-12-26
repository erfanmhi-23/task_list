from django.contrib import admin
from .models import Tasks

@admin.register(Tasks)
class taskadmin(admin.ModelAdmin):
    list_display = ('owner','title','discription', 'deadline', 'is_archived')
    list_filter = ('status', 'priority','is_archived')
    search_fields = ('owner__user__username','title')
