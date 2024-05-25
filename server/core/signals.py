from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PurchaseOrder
from .utils import calculate_performance_metrics


@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    calculate_performance_metrics(instance.vendor)
