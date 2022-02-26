from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name="list"),
     path('update_work/<str:pk>/', views.UpdateWork, name="update_work" )
]