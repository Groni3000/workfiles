from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path('completed_stories/', views.show_completed_stories, name='completed_stories'),
    path('result_of_search/', views.result_of_search_page, name='search_result'),
]
