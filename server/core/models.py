from django.db import models


# Create your models here.
class Vendor(models.Model):
    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"

    name = models.CharField("Vendor's Name", max_length=500, null=False)
    contact_details = models.TextField("Contact Details")
    address = models.TextField("Address")
    vendor_code = models.CharField("Vendor's Code", max_length=100, unique=True)
    on_time_delivery_rate = models.FloatField("On Time Delivery Rating", default=0)
    quality_rating_avg = models.FloatField("Quality Rating Avg", default=0)
    average_response_time = models.FloatField("Average Response Time", default=0)
    fulfillment_rate = models.FloatField("Fulfillment Rate", default=0)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    class Meta:
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)


class HistoricalPerformance(models.Model):
    class Meta:
        verbose_name = "Historical Performance"
        verbose_name_plural = "Historical Performance"
        
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
