from rest_framework import status
from rest_framework.test import APITestCase
from .polygon.models import ServiceAreaPolygon
from .provider.models import Providers
from django.contrib.gis.geos import Polygon, MultiPolygon

class ProviderTest(APITestCase):

    def setUp(self):
        self.payload = {
            'name': 'test', 'email': 'test1@test.com',
            'phone_no': "9971815575", 'language': 'en', 'currency': 'INR'}
        self.provider = Providers.objects.create(
            name="test",
            email="test@test.com",
            phone_no="7042828052",
            language="en",
            currency="USD")
        self.pk = self.provider.id
        self.endpoint = "/api/provider"

    def test_can_create_provider(self):
        endpoint = self.endpoint
        endpoint = "%s/create/" % (self.endpoint)
        response = self.client.post(endpoint, self.payload)
        self.assertEqual(response.status_code, 201)

    def test_can_update_provider(self):
        endpoint = "%s/%s/update/" % (self.endpoint, self.pk)
        payload = self.payload
        payload["name"] = "test123"
        response = self.client.put(endpoint, payload)
        self.assertEqual(response.status_code, 200)

    def test_can_retrieve_provider(self):
        endpoint = "%s/%s/" % (self.endpoint, self.pk)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)

    def test_can_add_servicearea(self):
        endpoint = "api/polygon/create/"
        mpoly = [[[28.463862268869118,76.85554504394531],[28.456618312416825,77.04574584960938],[28.566431608638386
,77.13706970214844],[28.603211564929566,77.04574584960938]]]
        polys = []    
        for poly_data in mpoly:
            #first node is last node
            poly_data.append(poly_data[0])
            poly = Polygon(poly_data)
            polys.append(poly)
        mpolys = MultiPolygon(polys)
        
        payload = {
            "mpoly": mpolys,
            "name": "Sector 18, Gurgaon",
            "price": 100,
            "provider_id":self.pk
        }
        response = self.client.post(endpoint, payload)
        
        self.assertEqual(response.status_code, 201)

    def test_can_view_servicearea(self):
        endpoint = "%s/%s/all/" %("api","polygon")
        response = self.client.get(endpoint)
        print "response = ", response
        self.assertEqual(response.status_code, 200)

    def test_can_delete_provider(self):
        endpoint = "%s/%s/delete/" % (self.endpoint, self.pk)
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, 204)



class ServiceAreaPolygonTest(APITestCase):
    def setUp(self):
        mpoly = [[[28.463862268869118,76.85554504394531],[28.456618312416825,77.04574584960938],[28.566431608638386
,77.13706970214844],[28.603211564929566,77.04574584960938]]]
        polys = []    
        for poly_data in mpoly:
            #first node is last node
            poly_data.append(poly_data[0])
            poly = Polygon(poly_data)
            polys.append(poly)
        mpolys = MultiPolygon(polys)

        self.payload = {
            "mpoly": mpoly,
            "name": "IGI, Delhi",
            "price": 100,
            "provider_id":1
        }
        self.payload_update = {
            "mpoly": mpolys,
            "name": "IGI, Delhi",
            "price": 100,
            "provider_id":1
        }
        self.provider = Providers.objects.create(
            name="test",
            email="test@testcheck.com",
            phone_no="70428280521",
            language="en",
            currency="INR")
        self.servicearea = ServiceAreaPolygon.objects.create(
            mpoly=mpolys,
            name="test",
            price="1000",
            provider_id=str(self.provider.id))
        self.pk = self.servicearea.id
        self.endpoint = "/api/polygon"

    def test_can_create_servicearea(self):
        endpoint = self.endpoint
        endpoint = "%s/create/" % (self.endpoint)
        response = self.client.post(endpoint, self.payload, format='json')
       
        self.assertEqual(response.status_code, 201)

    def test_can_update_servicearea(self):
        endpoint = "%s/%s/update/" % (self.endpoint, self.pk)
        payload = self.payload_update
        payload["name"] = "Gurgaon",
        payload["provider_id"] = str(self.provider.id)
        response = self.client.put(endpoint, payload)
        self.assertEqual(response.status_code, 200)

    def test_can_retrieve_servicearea(self):
        endpoint = "%s/%s/" % (self.endpoint, self.pk)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)

    def test_can_delete_servicearea(self):
        endpoint = "%s/%s/delete/" % (self.endpoint, self.pk)
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, 204)