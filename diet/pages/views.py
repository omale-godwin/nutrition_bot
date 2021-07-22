from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = name = request.POST['subject']
        message = request.POST['message']
        con = Contact(fname=fname, lname=lname, email=email, subject=subject, message=message)
        con.save()
        messages.success(request, 'contact submitted successfully')
        return redirect('contact')


    return render(request, 'pages/contact.html')
