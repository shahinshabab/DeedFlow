from django.contrib import admin
from .models import DocumentUpload


@admin.register(DocumentUpload)
class DocumentUploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'uploaded_by', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'uploaded_by__username')
    readonly_fields = ('created_at', 'updated_at')
