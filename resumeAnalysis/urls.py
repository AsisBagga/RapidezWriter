from django.urls import path, include
from . import views

app_name = 'resumeAnalysis'

urlpatterns = [
    path('', views.resume_analysis, name='resumeAnalysis'),
    path('resumeUpload/', views.resume_upload, name='resumeUpload'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('test/', views.test, name='test'),
]
