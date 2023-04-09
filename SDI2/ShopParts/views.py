from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])

def user_list(request, format=None):
	if request.method=='GET':
		users=User.objects.all()
		serializer=UserSerializer(users, many=True)
		return JsonResponse({'users':serializer.data})

	if request.method=='POST':
		serializer=UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])

def user_detail(request,id,format=None):
	try:
		user=User.objects.get(pk=id)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method=='GET':
		serializer=UserSerializer(user)
		return Response(serializer.data)
	elif request.method=='PUT':
		serializer=UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	elif request.method=='DELETE':
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])

def part_list(request, format=None):

	if request.method=='GET':
		price=request.GET.get('price')
		parts=Part.objects.all()
		if price:
			parts=parts.filter(price__gte=price)
		serializer=PartSerializer(parts, many=True)
		return JsonResponse({'parts':serializer.data})

	if request.method=='POST':
		serializer=PartSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])

def part_detail(request,id,format=None):
	try:
		part=Part.objects.get(pk=id)
	except Part.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method=='GET':
		serializer=PartSerializer(part)
		return Response(serializer.data)
	elif request.method=='PUT':
		serializer=PartSerializer(part, data=request.data)
		if serializer.is_valid():
			serializer.save
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	elif request.method=='DELETE':
		part.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])

def order_list(request, format=None):

	if request.method=='GET':
		orders=Order.objects.all()
		serializer=OrderSerializer(orders, many=True)
		return JsonResponse({'orders':serializer.data})

	if request.method=='POST':
		serializer=OrderSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])

def order_detail(request,id,format=None):
	try:
		order=Order.objects.get(pk=id)
	except Order.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method=='GET':
		serializer=OrderSerializer(Order)
		return Response(serializer.data)
	elif request.method=='PUT':
		serializer=OrderSerializer(order, data=request.data)
		if serializer.is_valid():
			serializer.save
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	elif request.method=='DELETE':
		order.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)