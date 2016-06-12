from rest_framework import serializers

from .models import Providers


class ProviderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Providers
        fields = [
            'id',
            'name',
            'email',
            'phone_no', 
            'language', 
            'currency'
            ]

class ProviderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Providers
        fields = [
            'name',
            'email',
            'phone_no', 
            'language', 
            'currency'
            ]

class ProviderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Providers
        fields = [
            'name',
            'email',
            'phone_no', 
            'language', 
            'currency'
            ]
