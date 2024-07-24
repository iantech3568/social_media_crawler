from django.shortcuts import render
from .models import SocialMediaPost

def home(request):
    posts = SocialMediaPost.objects.all()
    return render(request, 'crawler/home.html', {'posts': posts})
