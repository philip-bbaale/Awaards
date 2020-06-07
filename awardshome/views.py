from django.shortcuts import render, redirect
from awardsposts . models import Post
from awardsposts.forms import usability_rating, design_rating, content_rating
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@csrf_protect
def home(request):
    post = Post.objects.all().order_by('-last_modified')

    if request.method == 'POST':
        u_form = usability_rating(request.POST)
        d_form = design_rating(request.POST)
        c_form = content_rating(request.POST)
        if u_form.is_valid() and d_form.is_valid() and c_form.is_valid():
            u_form.save()
            d_form.save()
            c_form.save()
            return redirect('awards-home')

    else:
        u_form = usability_rating()
        d_form = design_rating()
        c_form = content_rating()

    context={
        'posts' : post,
        'u_form' : u_form,
        'd_form' : d_form,
        'c_form' : c_form,
    }
    return render(request, 'awardshome/home.html', context)

def about(request):
    return render(request, 'awardshome/about.html', {'title':'About'})
