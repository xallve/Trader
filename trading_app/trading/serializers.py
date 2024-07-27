from rest_framework import serializers
from .models import LimitOrder


class LimitOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LimitOrder
        fields = ['id', 'user', 'symbol', 'price', 'quantity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
