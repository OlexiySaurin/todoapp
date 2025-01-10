from django.contrib import admin
from django.urls import include, path, reverse
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("tasks.urls")),
    # django packages urls
    path('silk/', include('silk.urls', namespace='silk')),
    path('accounts/', include('allauth.urls')),
    path('api/', include("tasks.api.urls")),
] + debug_toolbar_urls()  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)