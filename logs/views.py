from django.shortcuts import render

def home(request):
    """Ray Logs home page"""

    return render(request, 'logs/home.html')