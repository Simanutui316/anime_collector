from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.http import HttpResponse
from .models import Anime, Va
from .forms import WatchingForm


class AnimeCreate(CreateView):
    model = Anime
    # fields = ['title', 'genre', 'description', 'seasons']
    fields = '__all__'
    # template_name = 'animes/index.html'

class AnimeUpdate(UpdateView):
      model = Anime
  # Let's disallow the renaming of a cat by excluding the name field!
      fields = '__all__'

class AnimeDelete(DeleteView):
  model = Anime
  success_url = '/animes/'

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
    vas_anime_doesnt_have = Va.objects.exclude(id__in = anime.vas.all().values_list('id'))
    watching_form = WatchingForm()
    return render(request, 'animes/detail.html', { 'anime': anime, 'watching_form': watching_form, 'vas': vas_anime_doesnt_have})

def add_watching(request, anime_id):
  form = WatchingForm(request.POST)
  if form.is_valid():
      new_watching = form.save(commit=False)
      new_watching.anime_id = anime_id
      new_watching.save()
  return redirect('detail', anime_id=anime_id)