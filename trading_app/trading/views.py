from rest_framework import generics, permissions
from .models import LimitOrder
from .serializers import LimitOrderSerializer
from .tasks import process_limit_order
from django.shortcuts import render


def index(request):
    return render(request, 'trading/index.html')


class LimitOrderListCreateView(generics.ListCreateAPIView):
    queryset = LimitOrder.objects.all()
    serializer_class = LimitOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save(user=self.request.user)
        process_limit_order.delay(order.id)


class LimitOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LimitOrder.objects.all()
    serializer_class = LimitOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)