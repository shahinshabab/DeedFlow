from django.db import models


class ExtractedText(models.Model):
    document = models.OneToOneField('documents.DocumentUpload', on_delete=models.CASCADE, related_name='extracted_text')
    raw_text = models.TextField()
    cleaned_text = models.TextField(blank=True)
    page_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Extracted text for {self.document_id}'
