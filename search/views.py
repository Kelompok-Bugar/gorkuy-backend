from django.shortcuts import render
from django.core import serializers
from database.models import Mitra
from django.http.response import HttpResponse

def index(request):
    data = serializers.serialize('json', Mitra.objects.all())
    return HttpResponse(data, content_type="application/json")

def search(request, keyword):
    results = Mitra.objects.filter(username=keyword)
    data = serializers.serialize('json', results)
    return HttpResponse(data, content_type="application/json")
