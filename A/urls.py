from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/home/', include('home.urls', namespace='home')),
    path('api/accounts/', include('accounts.urls', namespace='accounts')),
    path('api/evaluation/', include('evaluation.urls', namespace='evaluation')),
    path('api/journal/', include('journal.urls', namespace='journal')),
    path('api/recommender/', include('recommender.urls', namespace='recommender')),
    path('api/podcast/', include('podcast.urls', namespace='podcast')),
    path('api/programs/', include('programs.urls', namespace='programs')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)