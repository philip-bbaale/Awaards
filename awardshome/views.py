from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'awardshome/home.html')

def about(request):
    return render(request, 'awardshome/about.html', {'title':'About'})
