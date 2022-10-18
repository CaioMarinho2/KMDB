from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class ChoicesRecomendations(models.TextChoices):
    MUST_WATCH="Must Watch"
    SHOULD_WATCH="Should Watch"
    AVOID_WATCH="Avoid Watch"
    DEFAULT = "No Opinion"


class Review(models.Model):
    stars = models.IntegerField(validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    review=models.TextField()
    spoilers= models.BooleanField(default=False)
    recomendation= models.CharField(max_length=50,choices=ChoicesRecomendations.choices,default=ChoicesRecomendations.DEFAULT)
    
    movie=models.ForeignKey("movies.Movie",on_delete=models.CASCADE,related_name="reviews")
    critic=models.ForeignKey("user.User",on_delete=models.CASCADE,related_name="reviews")
    
