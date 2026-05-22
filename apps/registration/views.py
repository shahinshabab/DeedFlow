from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
from apps.core.constants import DOCUMENT_STATUS_REVIEWED
from .forms import RegistrationDraftReviewForm
from .models import RegistrationDraft


class RegistrationDraftListView(LoginRequiredMixin, ListView):
    model = RegistrationDraft
    template_name = 'registration/draft_list.html'
    context_object_name = 'drafts'
    paginate_by = 25

    def get_queryset(self):
        return RegistrationDraft.objects.select_related('document').filter(document__uploaded_by=self.request.user)


class RegistrationDraftDetailView(LoginRequiredMixin, DetailView):
    model = RegistrationDraft
    template_name = 'registration/draft_detail.html'
    context_object_name = 'draft'

    def get_queryset(self):
        return RegistrationDraft.objects.select_related('document').filter(document__uploaded_by=self.request.user)


class RegistrationDraftUpdateView(LoginRequiredMixin, UpdateView):
    model = RegistrationDraft
    form_class = RegistrationDraftReviewForm
    template_name = 'registration/draft_form.html'

    def get_queryset(self):
        return RegistrationDraft.objects.select_related('document').filter(document__uploaded_by=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        document = self.object.document
        document.status = DOCUMENT_STATUS_REVIEWED
        document.save(update_fields=['status', 'updated_at'])
        messages.success(self.request, 'Registration draft reviewed and saved.')
        return response

    def get_success_url(self):
        return reverse_lazy('registration:draft_detail', kwargs={'pk': self.object.pk})
