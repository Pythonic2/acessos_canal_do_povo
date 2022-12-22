from django.urls import path,include
from core import views
urlpatterns = [
   
    path('', views.CanalList.as_view(),name='canaldopovo'),
]

