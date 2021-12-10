from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'index.html')

def register(request):
    return render (request, 'login.html')

def inbox(request):
    return render (request, 'inbox.html')

def profile(request):
    return render(request, 'profile.html')

def groups(request):
    return render(request, 'groups.html')

def chart(request):
    return render(request, 'chart.html')