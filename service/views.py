from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from message.models import *
from message.forms import *
from .forms import *
from .models import *

# Create your views here.

def categorywise_mobile(request):
    mobile = MobilePhone.objects.all()
    context = {
        'mobile':mobile,
    }
    template = 'service/categorywise-service.html'
    return render(request, template, context)

def categorywise_compute(request):
    compute = Computing.objects.all()
    context = {
        'compute':compute,
    }
    template = 'service/categorywise-service.html'
    return render(request, template, context)

def categorywise_tv(request):
    tv = Television.objects.all()
    context = {
        'tv':tv,
    }
    template = 'service/categorywise-service.html'
    return render(request, template, context)

def categorywise_other(request):
    other = Others.objects.all()
    context = {
        'other':other,
    }
    template = 'service/categorywise-service.html'
    return render(request, template, context)

def categorywise_apartment(request):
    apartment = Apartment.objects.all()
    context = {
        'apartment':apartment,
    }
    template = 'service/categorywise-service.html'
    return render(request, template, context)

def categorywise_ecommerce(request):
    ecommerce = Ecommerce.objects.all()
    context = {
        'ecommerce':ecommerce,
    }
    template = 'service/categorywise-service.html'
    return render(request, template, context)

def categorywise_education(request):
    education = Education.objects.all()
    context = {
        'education':education,
    }
    template = 'service/categorywise-service.html'
    return render(request, template, context)

def searchingwise_service(request):
    query = request.GET.get("q", None)

    mobile = MobilePhone.objects.all()
    compute = Computing.objects.all()
    tv = Television.objects.all()
    other = Others.objects.all()
    apartment = Apartment.objects.all()
    ecommerce = Ecommerce.objects.all()
    education = Education.objects.all()

    if query is not None:
        mobile = mobile.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
                )
        compute = compute.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
                )
        tv = tv.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
                )
        other = other.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
                )
        apartment = apartment.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
                )
        ecommerce = ecommerce.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
                )
        education = education.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
                )

    context = {
        'mobile':mobile,
        'compute':compute,
        'tv':tv,
        'other':other,
        'apartment':apartment,
        'ecommerce':ecommerce,
        'education':education,
    }
    template = 'service/service-list.html'
    return render(request, template, context)

def service_list(request):
    mobile = MobilePhone.objects.all().order_by('-id')[:2]
    compute = Computing.objects.all().order_by('-id')[:2]
    tv = Television.objects.all().order_by('-id')[:2]
    other = Others.objects.all().order_by('-id')[:2]
    apartment = Apartment.objects.all().order_by('-id')[:2]
    ecommerce = Ecommerce.objects.all().order_by('-id')[:2]
    education = Education.objects.all().order_by('-id')[:2]

    context = {
        'mobile':mobile,
        'compute':compute,
        'tv':tv,
        'other':other,
        'apartment':apartment,
        'ecommerce':ecommerce,
        'education':education,
    }
    template = 'service/service-list.html'
    return render(request, template, context)

@login_required(login_url='login')
def create_mobilephone_service(request):
    form1 = MobilePhoneForm()
    if request.method == 'POST':
        form1 = MobilePhoneForm(request.POST, request.FILES)
        if form1.is_valid():
            obj = form1.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('detail_mobilephone_service', id=obj.id)
    context = {'form1':form1}
    template = 'service/add-service.html'
    return render(request, template, context)

def details_mobilephone_service(request, id):
    mobilephone = get_object_or_404(MobilePhone, id=id)
    comment = CommentMobilePhone.objects.filter(service__id=id)
    form1 = CommentMobilePhoneForm(request.POST or None)
    if request.method == 'POST':
        form1 = CommentMobilePhoneForm(request.POST, request.FILES)
        if form1.is_valid():
            obj = form1.save(commit=False)
            obj.service = mobilephone
            obj.save()
            return redirect('detail_mobilephone_service', id=id)
    context = {
        'mobilephone':mobilephone,
        'comment':comment,
        'form1':form1,
    }
    template = 'service/service-details.html'
    return render(request, template, context)

@login_required(login_url='login')
def edit_mobilephone_service(request, id):
    mobilephone = get_object_or_404(MobilePhone, id=id)
    form1 = MobilePhoneForm(instance=mobilephone)
    if request.method == 'POST':
        form1 = MobilePhoneForm(request.POST, request.FILES, instance=mobilephone)
        if form1.is_valid():
            obj = form1.save(commit=False)
            obj.save()
            return redirect('detail_mobilephone_service', id=obj.id)
    context = {'form1':form1}
    template = 'service/service-edit.html'
    return render(request, template, context)

@login_required(login_url='login')
def create_computing_service(request):
    form2 = ComputingForm()
    if request.method == 'POST':
        form2 = ComputingForm(request.POST, request.FILES)
        if form2.is_valid():
            obj = form2.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('detail_computing_service', id=obj.id)
    context = {'form2':form2}
    template = 'service/add-service.html'
    return render(request, template, context)

def details_computing_service(request, id):
    computing = get_object_or_404(Computing, id=id)
    comment = CommentComputing.objects.filter(service__id=id)
    form2 = CommentComputingForm(request.POST or None)
    if request.method == 'POST':
        form2 = CommentComputingForm(request.POST, request.FILES)
        if form2.is_valid():
            obj = form2.save(commit=False)
            obj.service = computing
            obj.save()
            return redirect('detail_computing_service', id=id)
    context = {
        'computing':computing,
        'comment':comment,
        'form2':form2,
    }
    template = 'service/service-details.html'
    return render(request, template, context)

@login_required(login_url='login')
def edit_computing_service(request, id):
    computing = get_object_or_404(Computing, id=id)
    form2 = ComputingForm(instance=computing)
    if request.method == 'POST':
        form2 = ComputingForm(request.POST, request.FILES, instance=computing)
        if form2.is_valid():
            obj = form2.save(commit=False)
            obj.save()
            return redirect('detail_computing_service', id=obj.id)
    context = {'form2':form2}
    template = 'service/service-edit.html'
    return render(request, template, context)

@login_required(login_url='login')
def create_television_service(request):
    form3 = TelevisionForm()
    if request.method == 'POST':
        form3 = TelevisionForm(request.POST, request.FILES)
        if form3.is_valid():
            obj = form3.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('detail_television_service', id=obj.id)
    context = {'form3':form3}
    template = 'service/add-service.html'
    return render(request, template, context)

def details_television_service(request, id):
    television = get_object_or_404(Television, id=id)
    comment = CommentTelevision.objects.filter(service__id=id)
    form3 = CommentTelevisionForm(request.POST or None)
    if request.method == 'POST':
        form3 = CommentTelevisionForm(request.POST, request.FILES)
        if form3.is_valid():
            obj = form3.save(commit=False)
            obj.service = television
            obj.save()
            return redirect('detail_television_service', id=id)
    context = {
        'television':television,
        'comment':comment,
        'form3':form3,
    }
    template = 'service/service-details.html'
    return render(request, template, context)

@login_required(login_url='login')
def edit_television_service(request, id):
    television = get_object_or_404(Television, id=id)
    form3 = TelevisionForm(instance=television)
    if request.method == 'POST':
        form3 = TelevisionForm(request.POST, request.FILES, instance=television)
        if form3.is_valid():
            obj = form3.save(commit=False)
            obj.save()
            return redirect('detail_television_service', id=obj.id)
    context = {'form3':form3}
    template = 'service/service-edit.html'
    return render(request, template, context)

@login_required(login_url='login')
def create_others_service(request):
    form4 = OthersForm()
    if request.method == 'POST':
        form4 = OthersForm(request.POST, request.FILES)
        if form4.is_valid():
            obj = form4.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('detail_others_service', id=obj.id)
    context = {'form4':form4}
    template = 'service/add-service.html'
    return render(request, template, context)

def details_others_service(request, id):
    others = get_object_or_404(Others, id=id)
    comment = CommentOthers.objects.filter(service__id=id)
    form4 = CommentOthersForm(request.POST or None)
    if request.method == 'POST':
        form4 = CommentOthersForm(request.POST, request.FILES)
        if form4.is_valid():
            obj = form4.save(commit=False)
            obj.service = others
            obj.save()
            return redirect('detail_others_service', id=id)
    context = {
        'others':others,
        'comment':comment,
        'form4':form4,
    }
    template = 'service/service-details.html'
    return render(request, template, context)

@login_required(login_url='login')
def edit_others_service(request, id):
    others = get_object_or_404(Others, id=id)
    form4 = OthersForm(instance=others)
    if request.method == 'POST':
        form4 = OthersForm(request.POST, request.FILES, instance=others)
        if form4.is_valid():
            obj = form4.save(commit=False)
            obj.save()
            return redirect('detail_others_service', id=obj.id)
    context = {'form4':form4}
    template = 'service/service-edit.html'
    return render(request, template, context)

@login_required(login_url='login')
def create_apartment_service(request):
    form5 = ApartmentForm()
    if request.method == 'POST':
        form5 = ApartmentForm(request.POST, request.FILES)
        if form5.is_valid():
            obj = form5.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('detail_apartment_service', id=obj.id)
    context = {'form5':form5}
    template = 'service/add-service.html'
    return render(request, template, context)


def details_apartment_service(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    comment = CommentApartment.objects.filter(service__id=id)
    form5 = CommentApartmentForm(request.POST or None)
    if request.method == 'POST':
        form5 = CommentApartmentForm(request.POST, request.FILES)
        if form5.is_valid():
            obj = form5.save(commit=False)
            obj.service = apartment
            obj.save()
            return redirect('detail_apartment_service', id=id)
    context = {
        'apartment':apartment,
        'comment':comment,
        'form5':form5,
    }
    template = 'service/service-details.html'
    return render(request, template, context)

@login_required(login_url='login')
def edit_apartment_service(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    form5 = ApartmentForm(instance=apartment)
    if request.method == 'POST':
        form5 = ApartmentForm(request.POST, request.FILES, instance=apartment)
        if form5.is_valid():
            obj = form5.save(commit=False)
            obj.save()
            return redirect('detail_apartment_service', id=obj.id)
    context = {'form5':form5}
    template = 'service/service-edit.html'
    return render(request, template, context)

@login_required(login_url='login')
def create_ecommerce_service(request):
    form6 = EcommerceForm()
    if request.method == 'POST':
        form6 = EcommerceForm(request.POST, request.FILES)
        if form6.is_valid():
            obj = form6.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('detail_ecommerce_service', id=obj.id)
    context = {'form6':form6}
    template = 'service/add-service.html'
    return render(request, template, context)


def details_ecommerce_service(request, id):
    ecommerce = get_object_or_404(Ecommerce, id=id)
    comment = CommentEcommerce.objects.filter(service__id=id)
    form6 = CommentEcommerceForm(request.POST or None)
    if request.method == 'POST':
        form6 = CommentEcommerceForm(request.POST, request.FILES)
        if form6.is_valid():
            obj = form6.save(commit=False)
            obj.service = ecommerce
            obj.save()
            return redirect('detail_ecommerce_service', id=id)
    context = {
        'ecommerce':ecommerce,
        'comment':comment,
        'form6':form6,
    }
    template = 'service/service-details.html'
    return render(request, template, context)

@login_required(login_url='login')
def edit_ecommerce_service(request, id):
    ecommerce = get_object_or_404(Ecommerce, id=id)
    form6 = EcommerceForm(instance=ecommerce)
    if request.method == 'POST':
        form6 = EcommerceForm(request.POST, request.FILES, instance=ecommerce)
        if form6.is_valid():
            obj = form6.save(commit=False)
            obj.save()
            return redirect('detail_ecommerce_service', id=obj.id)
    context = {'form6':form6}
    template = 'service/service-edit.html'
    return render(request, template, context)

@login_required(login_url='login')
def create_education_service(request):
    form7 = EducationForm()
    if request.method == 'POST':
        form7 = EducationForm(request.POST, request.FILES)
        if form7.is_valid():
            obj = form7.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('detail_education_service', id=obj.id)
    context = {'form7':form7}
    template = 'service/add-service.html'
    return render(request, template, context)


def details_education_service(request, id):
    education = get_object_or_404(Education, id=id)
    comment = CommentEducation.objects.filter(service__id=id)
    form7 = CommentEducationForm(request.POST or None)
    if request.method == 'POST':
        form7 = CommentEducationForm(request.POST, request.FILES)
        if form7.is_valid():
            obj = form7.save(commit=False)
            obj.service = education
            obj.save()
            return redirect('detail_education_service', id=id)
    context = {
        'education':education,
        'comment':comment,
        'form7':form7,
    }
    template = 'service/service-details.html'
    return render(request, template, context)

@login_required(login_url='login')
def edit_education_service(request, id):
    education = get_object_or_404(Education, id=id)
    form7 = EducationForm(instance=education)
    if request.method == 'POST':
        form7 = EducationForm(request.POST, request.FILES, instance=education)
        if form7.is_valid():
            obj = form7.save(commit=False)
            obj.save()
            return redirect('detail_education_service', id=obj.id)
    context = {'form7':form7}
    template = 'service/service-edit.html'
    return render(request, template, context)
