from django.views.generic import TemplateView



class AboutView(TemplateView):
    template_name = 'about.html'

class AboutLongView(TemplateView):
    template_name = 'elements.html'