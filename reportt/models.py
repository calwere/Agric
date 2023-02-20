from django.db import models
from django.contrib.gis.db import models
# from django.contrib.gis.utils import LayerMapping
# from .models import Roads

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=4326, null=True, blank=True)   
    # objects = models.GeoManager()

    def _unicode_ (self):
        return self.name
    
    class Meta:
        verbose_name_plural = " Incidences"

# class Roads(models.Model):
#     geom = models.LineStringField(srid=4326--mapping--multiple)


