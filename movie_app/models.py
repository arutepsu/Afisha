from django.db import models


# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    director = models.ForeignKey(
        "movie_app.Director",
        on_delete=models.CASCADE,
        verbose_name="director",
        related_name="directors"
    )

    def __str__(self):
        return f'{self.title} by {self.director}'


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(
        "movie_app.Movie",
        on_delete=models.CASCADE,
        verbose_name="review",
        related_name="reviews"
    )

    def __str__(self):
        return f'{self.text}'
