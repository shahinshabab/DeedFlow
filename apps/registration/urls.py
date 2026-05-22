from django.urls import path
from .views import RegistrationDraftDetailView, RegistrationDraftListView, RegistrationDraftUpdateView

app_name = 'registration'

urlpatterns = [
    path('drafts/', RegistrationDraftListView.as_view(), name='draft_list'),
    path('drafts/<int:pk>/', RegistrationDraftDetailView.as_view(), name='draft_detail'),
    path('drafts/<int:pk>/review/', RegistrationDraftUpdateView.as_view(), name='draft_update'),
]
