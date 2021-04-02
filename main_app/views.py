from django.shortcuts import render

from django.views.generic.edit import CreateView

from django.http import HttpResponse
from .models import Anime


class AnimeCreate(CreateView):
    model = Anime
    # fields = ['title', 'genre', 'description', 'seasons']
    fields = '__all__'
    # template_name = 'animes/index.html'

# animes = [
#     Anime('Haikyuu', 'Sports', 'Volleyball Anime', 4),
#     Anime('Jujutsu Kaisen', 'Supernatural/Action', 'Shounen Anime about Curses and Jujustsu Sorcerers', 1),
#     Anime('Black Clover', 'Magical/Action', 'Who will be the Wizard King', 1),
#     Anime('Attack On Titan', 'Science Fiction/Action', 'Humanity is on the brink of extinction', 4),

# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def animes_index(request):
    animes = Anime.objects.all()
    return render(request, 'animes/index.html', { 'animes': animes })

def animes_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    return render(request, 'animes/detail.html', { 'anime': anime})