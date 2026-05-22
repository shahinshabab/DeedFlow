from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='accounts:dashboard', permanent=False), name='home'),
    path('accounts/', include('apps.accounts.urls')),
    path('documents/', include('apps.documents.urls')),
    path('registration/', include('apps.registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
