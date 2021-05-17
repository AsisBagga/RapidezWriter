from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from resumeAnalysis.validators import validate_resume_ext_job
 
FAQ_CHOICES = (('About Us', 'About Us'),
                ('About Our Services', 'About Our Services'),
                ('About Our Writers', 'About Our Writers'),
                ('Help & Support', 'Help & Support')
              )

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

class FAQ(models.Model):
    category = models.CharField(max_length=300, choices=FAQ_CHOICES)
    heading = models.CharField(max_length=300)
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.heading

class Job(models.Model):
    heading = models.CharField(max_length=300)
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.heading

class SubmitJob(models.Model):
    job = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    resume = models.FileField(upload_to='JobResume/%Y/%m/%d/', validators=[validate_resume_ext_job])
    
    def __str__(self):
        return self.name
