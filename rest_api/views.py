from django.shortcuts import render
from .models import *

# rest framework
from .serializer import KrosovkaAPI
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

def home(request):
    return render(request, 'home.html')

# Api to'liq chiqarish
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def krosovksMakeAPI(request):
    krosovka = Krosovka.objects.all()
    serializer = KrosovkaAPI(krosovka, many=True)
    return Response(serializer.data)

    # API ni id orqali chiqarish (alohida, alohida)
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singleAPI(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializer = KrosovkaAPI(krosovka, many=False)
    return Response(serializer.data)

# Post joylash (Ma'lumot joylash)
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotjoylash(request):
    serializer = KrosovkaAPI(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

# Post update qilish
@api_view(["POST"])
@permission_classes((permissions.AllowAny, ))
def malumotUpdate(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    serializer = KrosovkaAPI(instance=krosovka, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

# Post delete qilish
@api_view(["DELETE"])
@permission_classes((permissions.AllowAny, ))
def malumotDelete(request, pk):
    krosovka = Krosovka.objects.get(id=pk)
    krosovka.delete()
        
    return Response("Muvaffaqiyatli o'chirildi")