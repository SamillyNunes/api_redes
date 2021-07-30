# Eh responsavel pela serializacao do objeto, ou seja, conversao do objeto da rede para o tipo JSON

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'price', 'store', 'category')
