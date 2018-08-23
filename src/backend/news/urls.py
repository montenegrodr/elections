from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListNews.as_view()),
    path('<int:pk>/', views.DetailNews.as_view()),
    path('aggregate_news/', views.aggregate_news)
]