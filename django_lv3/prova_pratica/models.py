from django.db import models

# Create your models here.

class Messaggio(models.Model):
    contatto=models.CharField(max_length=30)
    email=models.EmailField()
    oggetto=models.CharField(max_length=100)
    contenuto=models.TextField()

    def __str__(self):
        return self.oggetto