from django.urls import path
from .views import DocumentCreateView, DocumentDetailView, DocumentListView, DocumentProcessView

app_name = 'documents'

urlpatterns = [
    path('', DocumentListView.as_view(), name='list'),
    path('upload/', DocumentCreateView.as_view(), name='upload'),
    path('<int:pk>/', DocumentDetailView.as_view(), name='detail'),
    path('<int:pk>/process/', DocumentProcessView.as_view(), name='process'),
]
