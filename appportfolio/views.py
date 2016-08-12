from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'indexview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['github'] = 'https://github.com/KiaraRaynS'
        context['linkedin'] = 'https://www.linkedin.com/in/kiara-sherman-b83564125'
        return context


class PortfolioView(TemplateView):
    template_name = 'portfolioview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['link1'] = 'https://koquibilis.herokuapp.com/'
        context['code1'] = 'https://github.com/KiaraRaynS/koquibilis'
        context['code2'] = 'https://github.com/KiaraRaynS/urlshortner-06-16-16'
        return context
