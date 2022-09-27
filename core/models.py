from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="portfolio")
    description = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    url = models.CharField(max_length=100, null=True, blank=True)
    code_link = models.CharField(max_length=100, null=True, blank=True)
    made_with = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class SocailMediaLink(models.Model):
    fb = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    whatsapp = models.CharField(max_length=100, blank=True, null=True)
