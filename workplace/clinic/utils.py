import json


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