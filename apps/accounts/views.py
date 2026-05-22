from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.documents.models import DocumentUpload
from apps.registration.models import RegistrationDraft


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = DocumentUpload.objects.filter(uploaded_by=self.request.user)
        context['total_documents'] = qs.count()
        context['recent_documents'] = qs[:5]
        context['draft_count'] = RegistrationDraft.objects.filter(document__uploaded_by=self.request.user).count()
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
