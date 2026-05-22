from django import forms
from apps.core.forms import BootstrapModelForm
from .models import DocumentUpload


class DocumentUploadForm(BootstrapModelForm):
    class Meta:
        model = DocumentUpload
        fields = ['title', 'file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': 'application/pdf'}),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file and not file.name.lower().endswith('.pdf'):
            raise forms.ValidationError('Only PDF files are allowed.')
        return file
