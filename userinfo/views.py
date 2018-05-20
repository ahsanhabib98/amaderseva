from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm
from .models import Profile
from service.models import *

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    template = 'userinfo/profile.html'
                    return render(request, template)
    else:
        form = SignUpForm()
    template = 'userinfo/signup.html'
    context = {'form':form}
    return render(request, template, context)

@login_required(login_url='login')
def profile(request):
    template = 'userinfo/profile.html'
    return render(request, template)

@login_required(login_url='login')
def profile_create(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile-detail')
    context = {'form':form}
    template = 'userinfo/profile-create.html'
    return render(request, template, context)

def profile_detail(request):
    profile = get_object_or_404(Profile, user=request.user)

    mobile = MobilePhone.objects.filter(profile=profile)
    compute = Computing.objects.filter(profile=profile)
    tv = Television.objects.filter(profile=profile)
    other = Others.objects.filter(profile=profile)
    apartment = Apartment.objects.filter(profile=profile)
    ecommerce = Ecommerce.objects.filter(profile=profile)
    education = Education.objects.filter(profile=profile)

    context = {
        'profile':profile,
        'mobile':mobile,
        'compute':compute,
        'tv':tv,
        'other':other,
        'apartment':apartment,
        'ecommerce':ecommerce,
        'education':education,
        }
    template = 'userinfo/profile-detail.html'
    return render(request, template, context)

@login_required(login_url='login')
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/userinfo/profile-detail/')
    context = {'form':form}
    template = 'userinfo/profile-edit.html'
    return render(request, template, context)
