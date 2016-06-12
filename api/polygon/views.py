from .serializers import ( 
    PolygonListSerializer,
    PolygonUpdateSerializer,
    PolygonCreateSerializer
    )
from .models import ServiceAreaPolygon
from rest_framework.response import Response
from django.contrib.gis.geos import Polygon, MultiPolygon,Point
from rest_framework import status
from rest_framework.generics import ( 
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
    )

class PolygonListAPIView(ListAPIView):
    queryset = ServiceAreaPolygon.objects.all()
    serializer_class = PolygonListSerializer


class PolygonSearchAPIView(ListAPIView):
    queryset = ServiceAreaPolygon.objects.all()
    serializer_class = PolygonListSerializer

    def get(self, request):
        d = dict(request.GET)
        latlng = (float(request.GET['lat'].encode("utf-8")),float(request.GET['lng'].encode("utf-8")))
        point = Point(latlng)
        polygons = ServiceAreaPolygon.objects.filter(mpoly__contains=point)
        serializer = self.serializer_class(polygons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PolygonCreateAPIView(CreateAPIView):
    queryset = ServiceAreaPolygon.objects.all()
    serializer_class = PolygonCreateSerializer


    def get(self, request):
        polygons = ServiceAreaPolygon.objects.all()
        serializer = self.serializer_class(polygons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format='json'):
        data = request.data
        serializer = self.serializer_class(data=data)
        print 'serializer ==', serializer
        if serializer.is_valid():
            serializer.save()
            res_data = {"data": serializer.data}
            return Response(
                res_data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PolygonUpdateAPIView(UpdateAPIView):
    queryset = ServiceAreaPolygon.objects.all()
    serializer_class = PolygonUpdateSerializer
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        #import pdb;pdb.set_trace()
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print "instance = ",instance
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class PolygonDeleteAPIView(DestroyAPIView):
    queryset = ServiceAreaPolygon.objects.all()
    serializer_class = PolygonListSerializer
    lookup_field = "id"

class PolygonRetrieveAPIView(RetrieveAPIView):
    queryset = ServiceAreaPolygon.objects.all()
    serializer_class = PolygonListSerializer
    lookup_field = "id"

# Create your views here.

