from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('social', views.SocialMediaView.as_view(), name='social'),
    path('partner', views.PartnerLogoView.as_view(), name='partner'),
]
