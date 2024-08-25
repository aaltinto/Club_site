from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Serie(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name="Series")
    img = models.URLField(null=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True)
    production_date = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Season(models.Model):
    number = models.IntegerField()
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='serieName')

    def __str__(self):
        return f"{self.serie.name} Season {self.number}"

class Episode(models.Model):
    number = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='seasonNumber')
    rating = models.FloatField(null=True)
    link = models.URLField()

    def __str__(self):
        return f"{self.season.serie.name} Season {self.season.number} Episode {self.number}"
    