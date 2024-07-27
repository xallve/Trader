from celery import shared_task
from .models import LimitOrder


class Limit:
    pass


@shared_task
def process_limit_order(order_id):
    order = LimitOrder.objects.get(id=order_id)
