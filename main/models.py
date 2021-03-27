from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category

class Database(models.Model):
    heading = models.CharField(max_length=300)
    description = RichTextUploadingField(blank=True, null=True)
    pre_description = models.TextField()
    banner = models.ImageField(upload_to='images', blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.heading

class Testimonials(models.Model):
    name = models.CharField(max_length=300)
    profession = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    heading = models.CharField(max_length=300)
    description = models.CharField(max_length=3000)
    picture = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.heading