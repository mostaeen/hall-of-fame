from django.shortcuts import render
from django.views import generic
from .models import Hall, Video
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    return render(request, 'halls/home.html')


class CreateHallView(generic.CreateView):
    model = Hall
    template_name = 'halls/create.html'
    fields = ['title']
    success_url = reverse_lazy('home')


class CreateVideoView(generic.CreateView):
    model = Video
    template_name = 'halls/createvideo.html'
    fields = ['title', 'youtube_id', 'url', 'hall']
    success_url = reverse_lazy('home')
