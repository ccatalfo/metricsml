from django.db import models

class MetricsSourceType(models.Model):
    name = models.CharField(max_length=256)

class MetricsSource(models.Model):
    source_type = models.ForeignKey(MetricsSourceType)
    name = models.CharField(max_length=256)

class Metric(models.Model):
    source = models.ForeignKey(MetricsSource)
    time = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
