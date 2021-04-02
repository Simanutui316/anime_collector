from django.db import models
from django.urls import reverse
from datetime import date


SEEN = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)


# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    seasons = models.IntegerField()

    # new code below
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'anime_id': self.id})

class Watching(models.Model):
      date = models.DateField()
      seen = models.CharField(
          max_length=1, 
          choices=SEEN, 
          default=SEEN[0][0]
          )

      anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

      def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_seen_display()} on {self.date}"

      class Meta:
        ordering = ['-date']