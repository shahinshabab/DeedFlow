import json
from django import forms
from apps.core.forms import BootstrapModelForm
from apps.core.utils import pretty_json
from .models import RegistrationDraft


class RegistrationDraftReviewForm(BootstrapModelForm):
    reviewed_json = forms.CharField(
        label='Reviewed Registration JSON',
        widget=forms.Textarea(attrs={'rows': 22, 'class': 'form-control font-monospace'}),
        help_text='Edit this JSON after checking extracted data. Later this will become section-wise forms.',
    )

    class Meta:
        model = RegistrationDraft
        fields = ['reviewed_json']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        data = self.instance.reviewed_data or self.instance.structured_data or {}
        self.fields['reviewed_json'].initial = pretty_json(data)

    def clean_reviewed_json(self):
        value = self.cleaned_data['reviewed_json']
        try:
            return json.loads(value)
        except json.JSONDecodeError as exc:
            raise forms.ValidationError(f'Invalid JSON: {exc}')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.reviewed_data = self.cleaned_data['reviewed_json']
        instance.is_reviewed = True
        if commit:
            instance.save()
        return instance
