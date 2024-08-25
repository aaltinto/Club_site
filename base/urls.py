from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('series/<str:serie>/', views.serie, name='serie'),
    path('series/<str:serie>/season-<int:season>/episode-<int:number>', views.watch, name='episode'),
]
