from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("tasks.urls")),
    # django packages urls
    path('silk/', include('silk.urls', namespace='silk')),
    path('accounts/', include('allauth.urls')),
] + debug_toolbar_urls()