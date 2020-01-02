from django.shortcuts import render
from django.views.generic import TemplateView
from .utils import ObjectDetailMixin


def clinic(request):
    return render(request, 'main.html')


class Invest(ObjectDetailMixin, TemplateView):
    path = './static/json_pars/invest1.json'
    template_name = "hospital/invest.html"







