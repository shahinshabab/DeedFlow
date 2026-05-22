from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from .forms import DocumentUploadForm
from .models import DocumentUpload
from .services import process_uploaded_document


class DocumentListView(LoginRequiredMixin, ListView):
    model = DocumentUpload
    template_name = 'documents/document_list.html'
    context_object_name = 'documents'
    paginate_by = 25

    def get_queryset(self):
        return DocumentUpload.objects.filter(uploaded_by=self.request.user)


class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = DocumentUpload
    form_class = DocumentUploadForm
    template_name = 'documents/document_form.html'
    success_url = reverse_lazy('documents:list')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        messages.success(self.request, 'PDF uploaded successfully. Click Process to extract and structure the data.')
        return super().form_valid(form)


class DocumentDetailView(LoginRequiredMixin, DetailView):
    model = DocumentUpload
    template_name = 'documents/document_detail.html'
    context_object_name = 'document'

    def get_queryset(self):
        return DocumentUpload.objects.filter(uploaded_by=self.request.user)


class DocumentProcessView(LoginRequiredMixin, View):
    def post(self, request, pk):
        document = get_object_or_404(DocumentUpload, pk=pk, uploaded_by=request.user)
        try:
            draft = process_uploaded_document(document)
            messages.success(request, 'Document processed. Please review the registration draft.')
            return redirect('registration:draft_update', pk=draft.pk)
        except Exception as exc:
            messages.error(request, f'Processing failed: {exc}')
            return redirect(document.get_absolute_url())
