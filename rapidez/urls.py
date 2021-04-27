"""rapidez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from main import views
from ckeditor_uploader import views as uploader_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),

    path('signup/', views.signup, name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    #Service Pages
    path('resumeAnalysis/', include('resumeAnalysis.urls')),
    path('Resume-Consulting', views.resume_consulting, name="resumeConsulting"),
    path('Resume-Writing', views.resume_writing, name="resumeWriting"),
    path('Resume-Makeover', views.resume_makeover, name="resumeMakeover"),
    path('Resume-Makeover1', views.resume_makeover_1, name="resumeMakeover1"),
    path('Resume-Makeover2', views.resume_makeover_2, name="resumeMakeover2"),
    path('Resume-Makeover3', views.resume_makeover_3, name="resumeMakeover3"),
    path('Resume-Video', views.resume_video, name="resumeVideo"),
    path('linkedIn', views.linkedin, name="linkedIn"),
    path('quizes/<int:pk>', views.quizes, name="quizes"),
    path('quizes_list/', views.quizes_list, name="quizes_list"),

    # About Pages
    path('About', views.about, name="about"),
    path('Contact-Us', views.contact_us, name="contactUs"),
    path('search/', views.search, name="search"),

    #FAQ
    path('FAQ', views.faq, name="faq"),
    path('addFAQ/', views.addFAQ, name="addFAQ"),
    path('updateFAQ/<int:pk>', views.updateFAQ, name="updateFAQ"),
    path('deleteFAQ/<int:pk>', views.deleteFAQ, name="deleteFAQ"),

    #Testimonials
    path('Testimonials', views.testimonials, name="testimonials"),
    path('create-testimonial/', views.create_testimonial, name="create_testimonial"),
    path('update-testimonial/<int:pk>', views.testimonial_update, name="testimonial_update"),
    path('delete-testimonial/<int:pk>', views.testimonial_delete, name="testimonial_delete"),

    #Blog Pages
    path('create/', views.create_blog, name="create_blog"),
    path('update/<int:pk>', views.blog_update, name="blog_update"),
    path('delete/<int:pk>', views.blog_delete, name="blog_delete"),
    path('career-advise-list/', views.career_list_page, name="career_list_page"),
    path('career-advise-detail/<int:pk>', views.career_detail_page, name="career_detail_page"),
    path('career-advise-view-all/<str:key>', views.career_view_all_page, name="career_view_all_page"),
    path('view_category_wise/<str:filter>', views.view_category_wise, name="view_category_wise"),
    #CKEditor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^ckeditor/upload/', uploader_views.upload, name='ckeditor_upload'),
    # url(r'^ckeditor/browse/', never_cache(uploader_views.browse), name='ckeditor_browse'),

    # url(r'^upload/', staff_member_required(views.upload), name='ckeditor_upload'),
    # url(r'^browse/', never_cache(staff_member_required(views.browse)), name='ckeditor_browse'),

    # Category Creation and deletion 
    path('createCategory/', views.add_category, name="add_category"),
    path('deleteCategory/<int:pk>', views.delete_category, name="delete_category"),
    path('CategoryActions/', views.category_list_page, name="category_list_page"),

    # Payment Gateway Integration
    path('payment/', views.payment, name='payment'),
    path('payment_status/', views.payment_status, name='payment_status'),
    # path('payment_success/', views.payment_success, name='payment_success'),

    # Job Page
    path('Jobs/', views.job_page, name="job_page"),
    path('CreateJob/', views.addJob, name="addJob"),
    path('updateJob/<int:pk>', views.updateJob, name="updateJob"),
    path('deleteJob/<int:pk>', views.deleteJob, name="deleteJob"),
    path('SubmitApplication/<int:pk>', views.submitJob, name="submitJob"),

    #Privacy Policy and Terms&Conditions
    path('privacypolicy', views.privacypolicy, name="privacypolicy"),
    path('terms', views.terms, name="terms"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
