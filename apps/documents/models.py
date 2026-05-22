from django.conf import settings
from django.db import models
from django.urls import reverse
from apps.core.constants import DOCUMENT_STATUS_CHOICES, DOCUMENT_STATUS_UPLOADED


def upload_document_path(instance, filename):
    return f'uploaded_documents/user_{instance.uploaded_by_id}/{filename}'


class DocumentUpload(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to=upload_document_path)
    status = models.CharField(max_length=30, choices=DOCUMENT_STATUS_CHOICES, default=DOCUMENT_STATUS_UPLOADED)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='document_uploads')
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('documents:detail', kwargs={'pk': self.pk})
