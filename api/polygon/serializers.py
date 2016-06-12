from rest_framework import serializers

from .models import ServiceAreaPolygon
from api.provider.models import Providers
from django.contrib.gis.geos import Polygon, MultiPolygon
#from geojson import Polygon, MultiPolygon



class PolygonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceAreaPolygon
        fields = [
            'id',
            'name',
            'mpoly',
            'provider_id',
            'price'
            ]

class PolygonUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceAreaPolygon
        fields = [
            'name',
            'mpoly',
            'provider_id',
            'price'
            ]
"""
    def update(self, *args, **kwargs):
        polys = []    
        for poly_data in validated_data['mpoly']:
            #first node is last node
            poly_data.append(poly_data[0])
            poly = Polygon(poly_data)
            polys.append(poly)
        mpolys = MultiPolygon(polys)
        obj = ServiceAreaPolygon(
            name=validated_data['name'],
            provider_id=validated_data['provider_id'],
            price=validated_data['price'],
            mpoly=mpolys
            )
        obj.save()
        return obj
"""

class PolygonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAreaPolygon
        fields = [
            'name',
            'mpoly',
            'provider_id',
            'price'
            ]

    def validate_provider_id(self, provider_id):
        try:
            Providers.objects.get(id=provider_id)
            return provider_id
        except Providers.DoesNotExist:
            raise serializers.ValidationError("Invalid provider_id")

    def create(self, validated_data):
        polys = []    
        for poly_data in validated_data['mpoly']:
            #first node is last node
            poly_data.append(poly_data[0])
            poly = Polygon(poly_data)
            polys.append(poly)
        mpolys = MultiPolygon(polys)
        obj = ServiceAreaPolygon(
            name=validated_data['name'],
            provider_id=validated_data['provider_id'],
            price=validated_data['price'],
            mpoly=mpolys
            )
        obj.save()
        return obj
