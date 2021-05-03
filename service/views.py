import random
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer


class RandomRestaurantViewSet(viewsets.ViewSet):

    def list(self, request, format=None):
        objs = Restaurant.objects.all()
        restaurant = random.choice(objs)
        return Response({'name': restaurant.name, 'description': restaurant.description})
