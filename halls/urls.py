from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('halloffame/create', views.CreateHallView.as_view(), name='create_hall'),
    path('halloffame/createvideo',
         views.CreateVideoView.as_view(), name='create_video'),
]
