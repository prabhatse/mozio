from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import json

from .forms import AddProviderForm
from api.provider.models import Providers as Provider

class AddProvider(View):
    """
    Main view, show the map and receive a new service area and save it.
    """

    template_name = "provider/add_provider.html"

    def dispatch(self, *args, **kwargs):
        return super(AddProvider, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form':AddProviderForm()})

    def post(self, request):
        json_data = json.loads(request.body)
        form = AddProviderForm(json_data)
        if form.is_valid():
            form.save()
            data = {'saved': "Provider is Saved! please Add More"}
        else:
            data = {'errors': form.errors.values()}
        return HttpResponse(json.dumps(data), content_type="application/json")

add_provider = AddProvider.as_view()

