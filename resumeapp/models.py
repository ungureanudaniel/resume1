from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    text = RichTextField(blank=True, null=True)
    #text = models.TextField()

    def __str__(self):
        return self.text