from dataclasses import fields
from decimal import Decimal

from rest_framework import serializers

from store.models import Product, Collection


# declaring fields by my self
class CollectionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)

# geting field from the model
class ProductSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # inventory = serializers.IntegerField()

    # the ways you can return an object in another
    collection = CollectionSerializer()
    # collection = serializers.StringRelatedField()
    # collection =serializers.HyperlinkedRelatedField(
    #     queryset=Collection.objects.all(),
    #     view_name='collection-detail',
    # )


    discount = serializers.SerializerMethodField(method_name='discount_price')

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'inventory', 'discount','collection']

    # redefine it so it won,t show the default value which is the primary key
    def discount_price(self, product: Product):
        return product.price* Decimal(0.10)

class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [ 'title', 'price', 'description', 'inventory','collection']

