from django.shortcuts import render, redirect
from awardsposts . models import Post

# Create your views here.
def home(request):
    post = Post.objects.all().order_by('-last_modified')

    context={
        'posts' : post,
    }
    return render(request, 'awardshome/home.html', context)

def about(request):
    return render(request, 'awardshome/about.html', {'title':'About'})
