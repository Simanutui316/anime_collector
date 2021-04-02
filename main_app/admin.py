from django.contrib import admin
from .models import Anime, Watching, Va

# Register your models here.
admin.site.register(Anime)
# register the new Watching Model 
admin.site.register(Watching)
admin.site.register(Va)