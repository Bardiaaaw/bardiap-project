from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'message_preview', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'phone', 'message']
    readonly_fields = ['created_at']
    
    def message_preview(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'خلاصه پیام'