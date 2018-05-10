from django.db import models

# Create your models here.

class Paste(models.Model):
    paste_title = models.CharField(max_length=50)
    paste_language = models.CharField(max_length=25)
    paste_data = models.CharField(max_length=200)

    def __str__(self):
        return self.paste_title
