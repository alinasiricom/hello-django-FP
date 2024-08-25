from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import *

def index_view(request):
    return render(request, 'aapp/index.html')

def about_view(request):
    return render(request, 'aapp/about-us.html')


@csrf_protect
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Ticket successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Error ticket')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'aapp/contact-us.html', context)