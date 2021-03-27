from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

from .models import Database, Category, Testimonials, Quiz
from .forms import Databaseform, Categoryform, SignUpForm, Testimonialform
from django.db.models import Q

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

import razorpay

# SignUp Page
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



# General Page
def home(request):
    all_objects = Database.objects.all()
    return render(request,"home.html", {"blog":all_objects})
def about(request):
    return render(request,"about.html")
def contact_us(request):
    return render(request,"contact.html")
def faq(request):
    return render(request, "faq.html")

# Service Pages
def resume_consulting(request):
    return render(request,"resume_consulting.html")
def resume_writing(request):
    return render(request,"resume_writing.html")
def resume_makeover(request):
    return render(request,"resume_makeover.html")
def resume_makeover_1(request):
    return render(request,"resume_makeover1.html")
def resume_makeover_2(request):
    return render(request,"resume_makeover2.html")
def resume_makeover_3(request):
    return render(request,"resumeMakeover3.html")
def resume_video(request):
    return render(request,"resume_video.html")
def linkedin(request):
    return render(request,"linkedin.html")
def quizes(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    return render(request, "quiz.html", {"objects": quiz})
def quizes_list(request):
    all_objects = Quiz.objects.all()
    return render(request, "quizListPage.html", {"objects": all_objects})

# Create Blog
def create_blog(request):
    forms = Databaseform()
    if request.method == "POST":
        forms = Databaseform(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'createBlog.html', {'form': forms})
# Blog Listings
def career_list_page(request):
    all_objects = Database.objects.all()
    return render(request, 'career_list.html', {"objects": all_objects})
# Blog Page details
def career_detail_page(request, pk):
    category = Category.objects.all()
    blog = get_object_or_404(Database, pk=pk)
    return render(request, "career_detail.html",  {"blog_details":blog, "category":category})
# Update Blog
def blog_update(request, pk):
    blog = get_object_or_404(Database, pk=pk)
    forms = Databaseform(request.POST or None, instance = blog)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse( 'career_detail_page', args=[pk]))
        else:
            print(forms.errors.as_data())
    return render(request, "blogUpdate.html", {"forms":forms})  
# Delete a Blog
def blog_delete(request, pk):
    obj = get_object_or_404(Database, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('career_list_page'))
    return render(request, 'blogDelete.html')
#
def career_view_all_page(request):
    return render(request, "career_view_all.html")

# Categories
def add_category(request):
    forms = Categoryform()
    if request.method == "POST":
        forms = Categoryform(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'createBlogCategory.html', {'form': forms})
# Categories List Page
def category_list_page(request):
    all_objects = Category.objects.all()
    return render(request, 'category_list.html', {"objects": all_objects})
# Delete Category
def delete_category(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('career_list_page'))
    return render(request, 'blogDeleteCategory.html', {"obj":obj})
# View Blog Category wise
def view_category_wise(request, filter):
    category = Category.objects.all()
    filter = get_object_or_404(Category, category=filter)
    filter_op = Database.objects.filter(category=filter)
    return render(request, 'career_view_all.html', {'filter_op':filter_op, "filter":filter, "category":category})

# Testimonials CRUD
def testimonials(request):
    all_objects = Testimonials.objects.all()
    return render(request,"testimonials.html", {'objects':all_objects})

def create_testimonial(request):
    forms = Testimonialform()
    if request.method == "POST":
        forms = Testimonialform(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('testimonials'))
    return render(request, 'createTestimonial.html', {'form': forms})

def testimonial_update(request, pk):
    blog = get_object_or_404(Testimonials, pk=pk)
    forms = Testimonialform(request.POST or None, instance = blog)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('testimonials'))
        else:
            print(forms.errors.as_data())
    return render(request, "testimonialUpdate.html", {"forms":forms}) 

def testimonial_delete(request, pk):
    obj = get_object_or_404(Testimonials, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('testimonials'))
    return render(request, 'testimonialDelete.html')

#Payment Gateway integration
client = razorpay.Client(auth=("rzp_live_nQOflfXhoAJfEG", "rpKTqVpjezaNxt8SWXHjqQUg"))
def payment(request):
    print("Inside payment method")
    context = {}
    if request.method == "POST":
        print("Inside payment method if loop")
        order_amount = 200
        order_currency = 'INR'
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        template_id=request.POST.get('template_id')
        print("template_id: " + template_id)

        response = client.order.create({'amount': order_amount, 'currency': order_currency, 'payment_capture': '1'})
        order_id = response['id']
        order_status = response['status']
        print("Order Status Response: ")
        print(order_status)
        print("\n")

        print("Order ID  Response: ")
        print(order_id)
        print("\n")

        if order_status=='created':
            print("Order created")
            # context['price'] = order_amount
            # context['currency'] = order_currency
            context['name'] = name
            context['phone'] = phone
            context['email'] = email
            context['template_id'] = template_id

            # data that'll be send to the razorpay for
            context['order_id'] = order_id

            # return render(request, 'resume_makeover.html', {'context': context})
        else:
            return HttpResponse('<h1> Error in creating a payment order</h1>')
    
    response = request.POST
    print("Response of params_dict from Razorpay: ")
    print(response)
    print("\n")
    
    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }

        # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'payment_success.html', {'status': 'Payment Successful!'})
    except:
        return render(request, 'payment_failure.html', {'status': 'Payment Failure!'})  

def payment_status(request):

    response = request.POST
    print("Response of params_dict from Razorpay: ")
    print(response)
    print("\n")
    
    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }


    # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'payment_success.html', {'status': 'Payment Successful!'})
    except:
        return render(request, 'payment_failure.html', {'status': 'Payment Failure!'})    
def payment_success(request):
    return render(request, "payment_success.html")

def career_page(request):
    return render(request, "career_page.html")
