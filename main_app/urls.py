from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('anime/', views.animes_index, name='index'),
  path('anime/<int:anime_id>/', views.animes_detail, name='detail'),

]

