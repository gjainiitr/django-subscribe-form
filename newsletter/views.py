from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from newsletter.models import Subscribe
from django.contrib import messages
from datetime import datetime
# Create your views here.


def subscribe(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Subscribe(name=name, email=email)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'newsletter_form.html')
