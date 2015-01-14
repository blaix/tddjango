from django.views.generic.base import TemplateView


class PageView(TemplateView):
    template_name = 'page.html'
