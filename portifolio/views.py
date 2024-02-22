# portifolio/views.py
from django.shortcuts import render

def home(request):
    # Your view logic here
    return render(request, 'home.html')  # Adjust the template name as needed
