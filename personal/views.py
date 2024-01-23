from django.shortcuts import render, redirect
from .models import Tbcars
from personal.forms import TbcarsForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from personal.serializers import TbcarsSerializers
import math

# Create your views here.
# MONOLITH
def home_screen_view(request):
    print(request.headers)
    return render(request, "helloworld.html", {})

def crud1(request):
    print(request.headers)
    cars = Tbcars.objects.all()
    return render(request, "crudmono.html", {'cars':cars})

def add(request):
    if request.method == "POST":
        form = TbcarsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = TbcarsForm()
    return render(request, 'add.html', {'form':form})

def edit(request, id):
    cars = Tbcars.objects.get(id=id)
    return render(request, 'edit.html', {'cars':cars})

def update(request, id):
    cars = Tbcars.objects.get(id=id)
    form = TbcarsForm(request.POST, instance= cars)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'cars':cars})

def delete(request, id):
    cars = Tbcars.objects.get(id=id)
    cars.delete()
    return redirect('/')

#WEB SERVICE
@csrf_exempt
def tbcarsApi(request, id=0):
    if request.method == 'GET':
        cars = Tbcars.objects.all()
        cars_serializer = TbcarsSerializers(cars, many=True)
        return JsonResponse(cars_serializer.data, safe=False)
    elif request.method == 'POST':
        cars_data = JSONParser().parse(request)
        cars_serializer = TbcarsSerializers(data = cars_data)
        if cars_serializer.is_valid():
            cars_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed To Add", safe=False)
    elif request.method == 'PUT':
        cars_data = JSONParser().parse(request)
        cars = Tbcars.objects.get(id=cars_data['id'])
        cars_serializer = TbcarsSerializers(cars, data=cars_data)
        if cars_serializer.is_valid():
            cars_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed To Update")
    elif request.method == 'DELETE':
        cars = Tbcars.objects.get(id=id)
        cars.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
#RSA ALGORITHM
p = 3
q = 7
@csrf_exempt
def rsa(request):
    if request.method == 'GET':
        data = [
            {'p':p,
             'q':q}
            ]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        n = p*q
        phi = (p-1)*(q-1)
        e = 2
        while(e<phi):
            if math.gcd(e, phi) == 1:
                break
            else:
                e += 1
        k = 2
        d = ((k*phi)+1)/e
        pukey = e, n
        pvkey = d, n
        key = [
            {'Public Key': pukey,
             'Private Key': pvkey}
        ]
        return JsonResponse(key, safe=False)
msg = 11
@csrf_exempt
def encrypt(request):
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    while(e<phi):
        if math.gcd(e, phi) == 1:
            break
        else:
            e += 1
    pukey = e, n
    if request.method == 'POST':
        
        C = pow(msg, e)
        C = math.fmod(C, n)
        data = [
            {
                'Message': msg,
                'Public Key': pukey
            }
        ]
        return JsonResponse(data, safe=False)
@csrf_exempt
def decrypt(request):
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    while(e<phi):
        if math.gcd(e, phi) == 1:
            break
        else:
            e += 1
    k = 2
    d = ((k*phi)+1)/e
    pvkey = d, n
    C = pow(msg, e)
    C = math.fmod(C, n)
    if request.method == 'POST':        
        M = pow(C, d)
        M = math.fmod(M, n)
        data = [
            {
                'Message': M,
                'Private Key': pvkey
            }
        ]
        return JsonResponse(data, safe=False)
    
    