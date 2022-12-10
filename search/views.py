from django.shortcuts import render
from django.core import serializers
from database.models import Mitra, UserGorkuy, Lapangan
from django.http.response import HttpResponse
import json

def index(request):
    data = serializers.serialize('json', Mitra.objects.all())
    data_json = json.loads(data)
    for i in range(0,len(data_json)):
        lapangans = Lapangan.objects.filter(mitra=data_json[i]['pk'])
        lapangans_data = serializers.serialize('json', lapangans)
        lapangans_json = json.loads(lapangans_data)
        data_json[i]['fields']['lapangans'] = lapangans_json
    response = json.JSONEncoder().encode(data_json)
    return render(request, 'index.html', {"result":data_json})
    # return HttpResponse(response, content_type="application/json")

def search(request, keyword):
    mitras = Mitra.objects.filter(name__icontains=keyword, )
    data = serializers.serialize('json', mitras)
    data_json = json.loads(data)
    count = 0
    for i in range(0,len(data_json)):
        lapangans = Lapangan.objects.filter(mitra=data_json[i]['pk'])
        lapangans_data = serializers.serialize('json', lapangans)
        lapangans_json = json.loads(lapangans_data)
        data_json[i]['fields']['lapangans'] = lapangans_json
        count += len(lapangans_json)
    response = json.JSONEncoder().encode(data_json)

    return render(request, 'index.html', {"result":data_json, "size":count, "keyword":keyword,"is_search":True})
    # return HttpResponse(response, content_type="application/json")
