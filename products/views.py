from django.shortcuts import render

from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.serializers import *

# Create your views here.
class GetProducts(APIView):
    def get(self, request):
        # items = Images.objects.all()
        # serializer = ImageSerializer(items, many=True)
        # return Response(serializer.data)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)