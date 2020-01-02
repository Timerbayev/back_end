from django.shortcuts import render
from .models import Staffer
# from patients import forms
# import datetime
from django.views.generic import TemplateView, View
from .utils import ObjectDetailMixin, PersonDetailMixin


class Spec(ObjectDetailMixin, TemplateView):
    path = './static/json_pars/spec.json'
    template_name = "doctors/spec1.html"


def staffer(request):
    lst = Staffer.object.all()
    return render(request, 'doctors/doctor.html', {'lst': lst})


class Persons(PersonDetailMixin, TemplateView):
    Object = Staffer
    template = 'doctors/person.html'
    # def persons(request, slug):
    #     person = Staffer.object.get(slug__iexact=slug)
    #     return render(request, 'doctors/person.html', {'person': person})



