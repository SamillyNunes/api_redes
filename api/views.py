from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(APIView):
    """
    API de produtos
    """

    def get(self, request, id=None):
        """
        Retorna todos os elementos de produtos salvos no BD
        :return:
        """

        if(id!=None):
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        products = Product.objects.all() #recuperando todos objetos de produto do bd
        serializer = ProductSerializer(products, many=True)
        headers = {"teste":"teste resposta"}
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        """
        Esse metódo permite modificar um campo por vez.

        :param request: requisição vinda do cliente
        :param id: id do produto
        :return: Response()
        """
        product = Product.objects.get(id=id)

        data = request.data

        if("name" in data.keys()):
            product.name = data["name"]
        if ("price" in data.keys()):
            product.price = data["price"]
        if ("store" in data.keys()):
            product.store = data["store"]
        if ("category" in data.keys()):
            product.category = data["category"]

        product.save()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, id):
        """
        Esse metódo obriga que sejam modificados todos os campos do modelo, com excecao do id.

        :param request: requisição vinda do cliente
        :param id: id do produto para atualizar
        :return: Response()
        """
        product = Product.objects.get(id=id)

        data = request.data

        if('name' in data.keys() and 'price' in data.keys() and 'store' in data.keys() and 'category' in data.keys()):
            product.name = data["name"]
            product.price = data["price"]
            product.store = data["store"]
            product.category = data["category"]

            product.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, id):
        Product.objects.get(id=id).delete()
        return Response(status=status.HTTP_200_OK)