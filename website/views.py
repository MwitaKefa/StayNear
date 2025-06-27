from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def property_detail(request):
    return render(request, 'property_detail.html')
