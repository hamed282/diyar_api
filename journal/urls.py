from django.urls import path
from . import views


app_name = 'journal'
urlpatterns = [
    path('list/', views.JournalListView.as_view(), name='journal_list'),
    path('', views.JournalView.as_view(), name='journal'),
]
