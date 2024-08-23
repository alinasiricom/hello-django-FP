from django.shortcuts import render


def signup_view(request):
    return render(request, 'account/sign-up.html')


def login_view(request):
    return render(request, 'account/login.html')


def terms_view(request):
    return render(request, 'account/terms-conditions.html')