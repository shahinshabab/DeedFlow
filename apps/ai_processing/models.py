from django.db import models


class AIProcessingLog(models.Model):
    document = models.ForeignKey('documents.DocumentUpload', on_delete=models.CASCADE, related_name='ai_logs')
    model_name = models.CharField(max_length=100, blank=True)
    prompt_name = models.CharField(max_length=100, default='registration_extraction_v1')
    structured_data = models.JSONField(default=dict, blank=True)
    raw_response = models.TextField(blank=True)
    success = models.BooleanField(default=False)
    error_message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'AI log {self.pk} for document {self.document_id}'
