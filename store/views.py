from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.translation.template import context_re
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer, CreateProductSerializer


# Create your views here
class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

    # def get_queryset(self):
    #     return Product.objects.all()
    #
    # def serializer_class(self):
    #     return CreateProductSerializer

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

#
# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         # the context in the nextline was added cause of the hyperlink in serialize class and the name added in url
#
#         serializer = ProductSerializer(products, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = CreateProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT','PATCH','DELETE'])
# def product_details(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     if request.method == 'PUT':
#         serializer = CreateProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     if request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     if request.method == 'PATCH':
#         serializer = CreateProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view()
def collection_list(request):
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view()
def collection_details(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data,status=status.HTTP_200_OK)
