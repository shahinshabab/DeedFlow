from django.contrib import admin
from .models import RegistrationDraft


@admin.register(RegistrationDraft)
class RegistrationDraftAdmin(admin.ModelAdmin):
    list_display = ('document', 'is_reviewed', 'created_at', 'updated_at')
    list_filter = ('is_reviewed', 'created_at')
    search_fields = ('document__title',)
    readonly_fields = ('created_at', 'updated_at')
