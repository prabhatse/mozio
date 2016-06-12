from django.contrib.gis.db import models

class Providers(models.Model):
    """
        Represent the Providers data. .
    """ 

    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=11, unique=True)
    language = models.CharField(max_length=11)
    currency= models.CharField(max_length=11)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ["-created"]
    
    def __str__(self):
        return self.name