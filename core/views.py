from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'core/post_list.html', {'posts': posts})

def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'core/home.html', {'posts': posts})

def company(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'core/company.html', {'posts': posts})

def team(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'core/team.html', {'posts': posts})

def features(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'core/features.html', {'posts': posts})