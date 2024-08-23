from django.shortcuts import render

def index_view(request):
    return render(request, 'aapp/index.html')

def about_view(request):
    return render(request, 'aapp/about-us.html')

def contact_view(request):
    return render(request, 'aapp/contact-us.html')