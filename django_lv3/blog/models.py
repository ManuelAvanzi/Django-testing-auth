from django.db import models

# Create your models here.

class BlogPostModel(models.Model):
    titolo=models.CharField(max_length=40)
    contenuto=models.TextField()
    bozza=models.BooleanField()

    def __str__(self):
        return self.titolo+" "+self.contenuto