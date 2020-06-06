from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import PostForm
from .models import Post
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
@csrf_protect
def new_post(request):
    form = PostForm(request.POST,request.FILES)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = Post(
                project_title = form.cleaned_data["project_title"],
                project_image = form.cleaned_data["project_image"],
                project_description = form.cleaned_data["project_description"],
                project_url = form.cleaned_data["project_url"],
                author = request.user
            )
            
            post.save()

            post_name = form.cleaned_data.get('project_title')
            messages.success(request, f'Your post has been created for {post_name} !')
            return redirect('awards-home')
    else:
        form = PostForm()

    return render(request, 'awardsposts/newPost.html',{'form': form})


