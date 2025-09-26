from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Video
from .forms import VideoForm

def index(request):
    return render(request, 'index.html')

class VideosListCreateView(ListView, CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'videos.html'
    success_url = '/videos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        context['form'] = VideoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videos')
        return render(request, 'videos.html', {'form': form})