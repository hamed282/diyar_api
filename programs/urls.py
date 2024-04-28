from django.urls import path
from . import views


app_name = 'programs'
urlpatterns = [
    # path('list/', views.ProgramListView.as_view(), name='programs'),
    # path('', views.ProgramView.as_view(), name='programs'),
    path('category', views.CategoryListView.as_view(), name='category_list'),
    path('subcategory', views.SubCategoryListView.as_view(), name='subcategory_list'),
    path('category_program', views.CategoryProgramView.as_view(), name='category_programs'),
    path('subcategory_program', views.SubCategoryProgramView.as_view(), name='subcategory_programs'),
]
