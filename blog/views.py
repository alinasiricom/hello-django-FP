from django.shortcuts import render


def home_view(request):
    return render(request, 'blog/blog.html')


def single_view(request):
    context = {}
    return render(request, 'blog/single-blog.html', context)