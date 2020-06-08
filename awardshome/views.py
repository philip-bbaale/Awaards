from django.shortcuts import render, redirect
from awardsposts . models import Post
from awardsposts.forms import RatingForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@csrf_protect
def home(request):
    post = Post.objects.all().order_by('-last_modified')

    context={
        'posts' : post,
    }
    return render(request, 'awardshome/home.html', context)

def about(request):
    return render(request, 'awardshome/about.html', {'title':'About'})

@csrf_protect
def rating(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('awards-home')

    else:
        form = RatingForm()


    context={
        'post' : post,
        'form' : form,
    }
    return render(request, 'awardshome/rating.html', context)
