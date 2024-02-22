# jobs/views.py
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'home.html'
    # Add any additional logic specific to your Home view