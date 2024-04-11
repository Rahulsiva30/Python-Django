from django.http import JsonResponse
from .models import Drinks
from .serializer import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework import response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
   if request.method == 'GET':
    drinks = Drinks.objects.all()
    serializer = DrinkSerializer(drinks, many = True)
    return JsonResponse({'drinks': serializer.data})
   
   if request.method == 'POST':
     serializer = DrinkSerializer(data=request.data)
     if serializer.is_valid():
        serializer.save()
        return response(serializer.data, status=status.HTTP_201_CREATED)
     
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request,id):
   try:
    drink = Drinks.objects.get(pk=id)
   except Drinks.DoesNotExist:
    return response(status=status.HTTP_404_NOT_FOUND)
   
   if request.method == 'GET':
    serializer = DrinkSerializer(drink)
    return response(serializer.data)
   elif request.method == 'POST':
     pass
   elif request.method == 'DELETE':
     pass
  