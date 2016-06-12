from django import forms
from django.contrib.gis.geos import Polygon, MultiPolygon
from api.polygon.models import ServiceAreaPolygon as ServiceArea
from api.provider.models import Providers


class SelectServiceAreaForm(forms.Form):
    """
        Form to select the service area to play with in the "find" page.
    """
    service_area = forms.ModelChoiceField(queryset=ServiceArea.objects.all())


class ServiceAreaForm(forms.Form):
    """
        Form to save/edit a Service area.
    """

    name = forms.CharField(label='Service Name', required=False)

    price = forms.CharField(label='Price', required=False)

    provider_id = forms.ModelChoiceField(queryset=Providers.objects.all())

    def save(self, force_insert=False, force_update=False, commit=True):
        try:
            obj = ServiceArea.objects.get(name=self.data['name'],
                provider_id=self.data['provider_id'], price=self.data['price'])

        except:
            obj = ServiceArea(name=self.data['name'],
                provider_id=self.data['provider_id'], price=self.data['price'])
        polys = []

        for poly_data in self.data['mpoly']:
            #first node is last node
            poly_data.append(poly_data[0])
            poly = Polygon(poly_data)
            polys.append(poly)
        mpolys = MultiPolygon(polys)
        obj.mpoly = mpolys
        obj.save()
