from django.contrib.gis.db import models

class ServiceAreaPolygon(models.Model):
    """
        Represent the service area polygon. using django gis for future purposes,
    this helps with the speed of the search and db lookups.
    """
    name = models.CharField(max_length=100, unique=True)
    mpoly = models.MultiPolygonField()
    price = models.CharField(max_length=5)
    provider_id = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.GeoManager()

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.name