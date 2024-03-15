from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


app_name = 'urls.py'
urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),

]
