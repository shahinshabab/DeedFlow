from django.db import models
from django.urls import reverse


class RegistrationDraft(models.Model):
    document = models.OneToOneField('documents.DocumentUpload', on_delete=models.CASCADE, related_name='registration_draft')
    structured_data = models.JSONField(default=dict, blank=True)
    reviewed_data = models.JSONField(default=dict, blank=True)
    is_reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'Registration draft for {self.document.title}'

    def get_absolute_url(self):
        return reverse('registration:draft_update', kwargs={'pk': self.pk})
