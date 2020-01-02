import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404


class ObjectDetailMixin:
    path = None
    template = 'None'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open(self.path, "r") as file:
            data = json.load(file)
            assert isinstance(data, list), 'should be type of list'
        context['lst'] = data
        return context


class PersonDetailMixin:
    Object = 'None'
    template = 'None'

    def get(self, request, slug):
        ob = get_object_or_404(self.Object, slug__iexact=slug)
        return render(request, self.template, {self.Object.__name__.lower(): ob})


