from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse
from service.models import Category
from message.forms import ContactForm
from userinfo.models import Profile


def home(request):
    category = Category.objects.all()
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ahredoan@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Your message not send!!!! Please try again.')
            messages.success(request, "Thank you for message us !")
            return redirect('home')
    context = {
        'form':form,
        'category':category,
    }
    template = 'home.html'
    return render(request, template, context)
