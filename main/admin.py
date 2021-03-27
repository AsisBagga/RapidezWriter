from django.contrib import admin
from .models import Database, Category, Testimonials, Quiz, FAQ, Job, SubmitJob

# Register your models here.
admin.site.register(Database)
admin.site.register(Category)
admin.site.register(Testimonials)
admin.site.register(Quiz)
admin.site.register(FAQ)
admin.site.register(Job)
admin.site.register(SubmitJob)