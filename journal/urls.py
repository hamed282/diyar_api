from django.urls import path
from . import views


app_name = 'journal'
urlpatterns = [
    path('list/', views.JournalView.as_view(), name='journal'),
    path('', views.JournalShowView.as_view(), name='journal_show'),
]
