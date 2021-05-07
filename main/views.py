from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404

from .models import Database, Category, Testimonials, Quiz, FAQ, Job
from .forms import Databaseform, Categoryform, SignUpForm, Testimonialform, FAQForm, JobForm, SubmitJobForm
from django.db.models import Q

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail

from rapidez import settings
from django.db.models import Q

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
def contact_us_original(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        services = request.POST.getlist('services')
        query = request.POST.get('message')
        email_from = settings.EMAIL_FROM
        email_to = settings.EMAIL_ADMIN
        servicesstr = " | ".join(services)
        print("Details: ", name, phone, email, servicesstr, query)
        
        text_content = "\n Name: "+name+"\n Email: "+email+"\n Phone Number: "+phone+"\n Services: "+servicesstr + "\n Query: "+query
        isSuccess = send_mail(
            'Customer Contact',
            text_content,
            email_from,
            [email_to],
            fail_silently=False,
        )
        print("Email sent : ", isSuccess)
        if isSuccess == True :
            return render(request,"thankyou_contact.html")
        else:
            return render(request,"failure_contact.html")
    return render(request, "contact.html")

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        services = request.POST.getlist('services')
        query = request.POST.get('message')
        email_from = settings.EMAIL_FROM
        email_to="bharath.nr1@gmail.com"
        servicesstr = " | ".join(services)
        print("Details: ", name, phone, email, servicesstr, query)
        
        text_content = "\n Name: "+name+"\n Email: "+email+"\n Phone Number: "+phone+"\n Services: "+servicesstr + "\n Query: "+query
        isSuccess = send_mail(
            'Customer Contact',
            text_content,
            email_from,
            [email_to],
            fail_silently=False,
        )
        print("Email sent : ", isSuccess)
        if isSuccess == True :
            return render(request,"thankyou_contact.html")
        else:
            return render(request,"failure_contact.html")
    return render(request, "contact.html")
    
#FAQ
def faq(request):
    all_objects = FAQ.objects.all()
    return render(request, "faq.html", {'objects':all_objects})

def addFAQ(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FAQForm()
    return render(request, 'createBlog.html', {'form':form})

def updateFAQ(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    forms = FAQForm(request.POST or None, instance = faq)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('faq'))
        else:
            print(forms.errors.as_data())
    return render(request, "blogUpdate.html", {"forms":forms})  

def deleteFAQ(request, pk):
    obj = get_object_or_404(FAQ, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('faq'))
    return render(request, 'blogDelete.html')

# Service Pages
def resume_consulting(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        services = request.POST.getlist('services')
        query = request.POST.get('message')
        email_from = settings.EMAIL_FROM
        email_to = settings.EMAIL_ADMIN
        servicesstr = " | ".join(services)
        print("Details: ", name, phone, email, servicesstr, query)
        
        text_content = "\n Name: "+name+"\n Email: "+email+"\n Phone Number: "+phone+"\n Services: "+servicesstr + "\n Query: "+query
        print(text_content)
        isSuccess = send_mail(
            'Customer Contact',
            text_content,
            email_from,
            [email_to],
            fail_silently=False,
        )
        print("Email sent : ", isSuccess)
        if isSuccess == True :
            return render(request,"thankyou_contact.html")
        else:
            return render(request,"failure_contact.html")
    return render(request,"resume_consulting.html")

def resume_writing(request):
    faq = FAQ.objects.filter(category='Help & Support')
    return render(request,"resume_writing.html", {'faqs':faq})
def resume_makeover(request):
    faq = FAQ.objects.filter(category='Help & Support')
    return render(request,"resume_makeover.html", {'faqs':faq})
def resume_makeover_1(request):
    faq = FAQ.objects.filter(category='Help & Support')
    return render(request,"resume_makeover1.html", {'faqs':faq})
def resume_makeover_2(request):
    faq = FAQ.objects.filter(category='Help & Support')
    return render(request,"resume_makeover2.html", {'faqs':faq})
def resume_makeover_3(request):
    faq = FAQ.objects.filter(category='Help & Support')
    return render(request,"resumeMakeover3.html", {'faqs':faq})
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
    category = Category.objects.all()
    test = dict()
    for i in category:
        test[i] = Database.objects.filter( category=i )
    return render(request, 'career_list.html', {"all_objects": all_objects, "test": test})

# View Blog Category wise
def career_view_all_page(request, key):
    filter = get_object_or_404(Category, category=key)
    all_objects = Database.objects.filter( category=filter)
    category = Category.objects.all()
    return render(request, "career_view_all.html", {"all_objects": all_objects, "category":category, "filter":filter})

def view_category_wise(request, filter):
    filter = get_object_or_404(Category, category=filter)
    all_objects = Database.objects.filter(category=filter)
    category = Category.objects.all()
    return render(request, 'career_view_all.html', {'all_objects':filter_op, "category":category, "filter":filter})

# Blog Page details
def career_detail_page(request, pk):
    category = Category.objects.all()
    blog = get_object_or_404(Database, pk=pk)
    related_article=[]
    for i in category:
        related_article.append( Database.objects.filter( category=i ))
    return render(request, "career_detail.html",  {"blog_details":blog, "category":category, "related_article":related_article})
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
    context = {}
    if request.method == "POST":
        print("Inside payment method if loop")
        order_amount = 200
        order_currency = 'INR'
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        template_id=request.POST.get('template_id')
        template_photo=request.POST.get('template_photo')
        template_price=request.POST.get('template_price')
        print("template_price: " + template_price)

        response = client.order.create({'amount': template_price, 'currency': order_currency, 'payment_capture': '1'})
        order_id = response['id']
        order_status = response['status']
        print("response: ", response)

        if order_status=='created':
            print("Order created: ")
            print(order_id)
            context['name'] = name
            context['phone'] = phone
            context['email'] = email
            context['template_id'] = template_id
            context['template_photo'] = template_photo
            context['template_price'] = template_price
            context['order_id'] = order_id

            return render(request, 'order_summary.html', {'context': context})
    return HttpResponse('<h1> Error in creating a payment order</h1>')

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

#Jobs
def job_page(request):
    all_objects = Job.objects.all()
    return render(request, "job_page.html", {'objects':all_objects})

def addJob(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'createBlog.html', {'form':form})

def updateJob(request, pk):
    job = get_object_or_404(Job, pk=pk)
    forms = JobForm(request.POST or None, instance = job)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('job_page'))
        else:
            print(forms.errors.as_data())
    return render(request, "blogUpdate.html", {"forms":forms})  

def deleteJob(request, pk):
    obj = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('job_page'))
    return render(request, 'blogDelete.html')

def submitJob(request, pk):
    obj = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = SubmitJobForm(request.POST, request.FILES)
        if form.is_valid():
            saved = form.save(commit=False)
            saved.job = str(obj.heading)
            print("name: "+saved.name+" email: "+saved.email+" phone: "+saved.phone + " Job: "+saved.job )
            saved.save()
            email_from = settings.EMAIL_FROM
            email_to = 'bharath.nr1@gmail.com'
            text_content = "name: "+saved.name+" email: "+saved.email+" phone: "+saved.phone + " Job: "+saved.job 
            isSuccess = send_mail(
                'New Job Profile Application',
                text_content,
                email_from,
                [email_to],
                fail_silently=False,
            )
            isSuccess.attach(saved.resume)
            isSuccess.send()
            # You might be confusted to see that I dont save the field, its because i dont care, I just worked too much on getting 
            # this content here and now i have realized i could have done this without models. But, now i dont have time to change it
            # SO chuck it.
            return HttpResponseRedirect(reverse('job_page'))
        else:
            print(form.errors.as_data())
    else:
        form = SubmitJobForm()
    return render(request, 'submitJob.html', {'form': form})

def search(request):
    category = Category.objects.all()
    try:
        query = request.GET.get('query')
        objects = Database.objects.filter( Q(heading__icontains=query) | Q(description__icontains=query))
    except:
        query = None
    if query:
        context={"objects":objects, "category":category}
        template="search.html"
    else:
        template="search.html"
        context={"category":category}
    return render(request, template, context)

def privacypolicy(request):
    return render(request, "privacypolicy.html")

def terms(request):
    return render(request, "terms.html")    
