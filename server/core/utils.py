from django.db.models import F, ExpressionWrapper, DurationField
from datetime import timedelta
from .models import PurchaseOrder, Vendor


def calculate_performance_metrics(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')

    # On-Time Delivery Rate
    on_time_deliveries = completed_orders.filter(delivery_date__lte=F('acknowledgment_date')).count()
    total_completed_orders = completed_orders.count()
    vendor.on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100 if total_completed_orders > 0 else 0

    # Quality Rating Average
    quality_ratings = completed_orders.exclude(quality_rating__isnull=True).values_list('quality_rating', flat=True)
    vendor.quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0

    # Average Response Time
    response_times = completed_orders.exclude(acknowledgment_date__isnull=True).annotate(
        response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=DurationField())
    ).values_list('response_time', flat=True)
    vendor.average_response_time = sum(response_times, timedelta()).total_seconds() / len(response_times) if response_times else 0

    # Fulfillment Rate
    successful_orders = completed_orders.filter(status='completed', quality_rating__isnull=False)
    vendor.fulfillment_rate = (successful_orders.count() / total_completed_orders) * 100 if total_completed_orders > 0 else 0

    vendor.save()


def get_vendor_performance_metrics(vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return None

    # Calculate performance metrics
    calculate_performance_metrics(vendor)

    # Return performance metrics
    return {
        'on_time_delivery_rate': vendor.on_time_delivery_rate,
        'quality_rating_avg': vendor.quality_rating_avg,
        'average_response_time': vendor.average_response_time,
        'fulfillment_rate': vendor.fulfillment_rate
    }