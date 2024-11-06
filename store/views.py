from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.translation.template import context_re
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Product, Collection, Review, ShoppingCart
from .serializers import ProductSerializer, CollectionSerializer, CreateProductSerializer, CreateCollectionSerializer, \
    ReviewSerializer, CreateShoppingCartSerializer


# Create your views here
# class ProductListAPIView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = CreateProductSerializer
#
#     # def get_queryset(self):
#     #     return Product.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return ProductSerializer
#         elif self.request.method == 'POST':
#             return CreateProductSerializer
#
# class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = CreateProductSerializer

# class CollectionListAPIView(ListCreateAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CreateCollectionSerializer
#
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return CollectionSerializer
#         elif self.request.method == 'POST':
#             return CreateCollectionSerializer
#
# class CollectionDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CreateCollectionSerializer

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_pk = self.request.query_params.get('product_pk')
        return Review.objects.filter(product_id = product_pk)

class ShoppingCartViewSet(viewsets.ViewSet):
    queryset = ShoppingCart.objects.all()
    serialize_class = CreateShoppingCartSerializer

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

# @api_view()
# def collection_list(request):
#     collections = Collection.objects.all()
#     serializer = CollectionSerializer(collections, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
# @api_view()
# def collection_details(request, pk):
#     collection = get_object_or_404(Collection, pk=pk)
#     serializer = CollectionSerializer(collection)
#     return Response(serializer.data,status=status.HTTP_200_OK)
