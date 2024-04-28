from django.urls import path
from . import views


app_name = 'recommender'
urlpatterns = [
    path('personal/', views.PersonalInformationView.as_view(), name='personal'),
    path('income/', views.IncomeView.as_view(), name='income'),
    path('skill/', views.SkillView.as_view(), name='skill'),
    path('job/', views.JobRecordView.as_view(), name='job'),
    path('education/', views.EducationalRecordView.as_view(), name='education'),
    path('recommender/', views.RecommenderView.as_view(), name='recommender_result'),
]
