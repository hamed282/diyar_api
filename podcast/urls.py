from django.urls import path
from . import views


app_name = 'podcast'
urlpatterns = [
    path('list/', views.PodcastView.as_view(), name='podcast'),
]
