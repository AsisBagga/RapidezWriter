from django import forms
from .models import Database, Category, Testimonials, FAQ, Job, SubmitJob
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Databaseform(forms.ModelForm):
    class Meta:
        model = Database
        fields = ('heading',
                  'description',
                  'banner',
                  'category')

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class Testimonialform(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = '__all__'

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class FAQForm(forms.ModelForm):
    class Meta:
        model=FAQ
        fields = '__all__'
    
class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields = '__all__'

class SubmitJobForm(forms.ModelForm):
    class Meta:
        model=SubmitJob
        fields = ('name', 'email', 'phone', 'resume') 