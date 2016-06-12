from .serializers import ( 
	ProviderListSerializer,
	ProviderUpdateSerializer,
	ProviderCreateSerializer
	)
from .models import Providers

from rest_framework.generics import ( 
	ListAPIView,
	RetrieveAPIView,
	CreateAPIView,
	DestroyAPIView,
	UpdateAPIView
	)

class ProviderRetrieveAPIView(RetrieveAPIView):
	queryset = Providers.objects.all()
	serializer_class = ProviderListSerializer
	lookup_field = "id"

class ProviderListAPIView(ListAPIView):
	queryset = Providers.objects.all()
	serializer_class = ProviderListSerializer

class ProviderCreateAPIView(CreateAPIView):
	queryset = Providers.objects.all()
	serializer_class = ProviderCreateSerializer


class ProviderUpdateAPIView(UpdateAPIView):
	queryset = Providers.objects.all()
	serializer_class = ProviderUpdateSerializer
	lookup_field = "id"

class ProviderDeleteAPIView(DestroyAPIView):
	queryset = Providers.objects.all()
	serializer_class = ProviderListSerializer
	lookup_field = "id"
