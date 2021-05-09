from django.db import models

# Create your models here.
class Delivery(models.Model):
    identifier=models.IntegerField()
    imported_id=models.CharField(max_length=50, blank=True, null=True)
    tracking_number=models.CharField(max_length=50, blank=True, null=True)
    status=models.JSONField()
    customer=models.JSONField()
    shipping_address=models.JSONField()
    label=models.JSONField()
    country = models.CharField(max_length=50, blank=True, null=True)
    carrier = models.CharField(max_length=50, blank=True, null=True)
    service = models.CharField(max_length=50, blank=True, null=True)
    barcodes = models.CharField(max_length=50, blank=True, null=True)
    deadline_at = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.CharField(max_length=50, blank=True, null=True)
    