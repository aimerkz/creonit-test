from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
