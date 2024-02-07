from django.urls import path
from . import views


app_name = 'recommender'
urlpatterns = [
    path('result/', views.RecommenderResultView.as_view(), name='recommender_result'),
]
