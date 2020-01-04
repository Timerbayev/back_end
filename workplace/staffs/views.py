from django.shortcuts import render
from .models import Staffer
# from patients import forms
# import datetime
from django.views.generic import TemplateView, View
from .utils import ObjectDetailMixin, PersonDetailMixin, ListMixin


class Spec(ObjectDetailMixin, TemplateView):
    path = './static/json_pars/spec.json'
    template_name = "staffers/spec1.html"


class Persons(PersonDetailMixin, TemplateView):
    Object = Staffer
    template = 'hospital/person.html'
    # def persons(request, slug):
    #     person = Staffer.object.get(slug__iexact=slug)
    #     return render(request, 'staffers/person.html', {'person': person})


class Staff(ListMixin, TemplateView):
    Object = Staffer
    template = 'staffers/staffer.html'

    # lst = Staffer.object.all()
    # return render(request, 'staffers/admins.html', {'lst': lst})








