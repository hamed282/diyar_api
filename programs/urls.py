from django.urls import path
from . import views


app_name = 'programs'
urlpatterns = [
    path('list/', views.ProgramListView.as_view(), name='programs'),
]
