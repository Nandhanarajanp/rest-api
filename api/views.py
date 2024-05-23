from django.shortcuts import render
from  rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from.serializers import *
from rest_framework import status

@api_view()
def hello_world(request):
    return Response({"message":"hello,world!"})


@api_view(['GET'])
def productlist(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializers(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET', 'POsT'])
def productadd(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializers(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer=ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def productview(request,product_id):
    product =Product.objects.get(id=product_id)
    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['GET','DELETE'])
def product_delete(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','PUT'])
def productedit(request,product_id):
    product=Product.objects.get(id=product_id)
    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializers(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PATCH'])
def productedit2(request,product_id):
    product=Product.objects.get(id=product_id)
    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = ProductSerializers(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    
@api_view(['GET'])
def detailslist(request):
    if request.method == 'GET':
        detail=Details.objects.all()
        serializer = DetailsSerializers(detail,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
@api_view(['POST'])
def detailsadd(request):
    if request.method == 'POST':
        serializer=DetailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def detailsview(request,details_id):
    detail=Details.objects.get(id=details_id)
    if request.method == 'GET':
        serializer = DetailsSerializers(detail)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    

@api_view(['GET','DELETE'])
def details_delete(request,detail_id):
    detail = Details.objects.get(id=detail_id)
    if request.method == 'GET':
        serializer = DetailsSerializers(detail)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT'])
def detailsedit(request,details_id):
    detail=Details.objects.get(id=details_id)
    if request.method == 'GET':
        serializer = DetailsSerializers(detail)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = DetailsSerializers  (detail,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST','GET'])
def caradd(request):
    if request.method == 'GET':
        cars=Car.objects.all()
        serializer = CarSerializers(cars,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CarSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE'])
def cardelete(request,car_id):
    car=Car.objects.get(id=car_id)
    if request.method == 'GET':
        serializer = CarSerializers(car)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        car.delete()
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','PUT'])
def caredit(request,car_id):
    car=Car.objects.get(id=car_id)
    if request.method == 'GET':
        serializer = CarSerializers(car)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CarSerializers(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PATCH'])
def caredit2(request,car_id):
    car=Car.objects.get(id=car_id)
    if request.method == 'GET':
        serializer = CarSerializers(car)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = CarSerializers(car,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





