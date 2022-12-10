from django.shortcuts import render
from database.models import Jadwal, Lapangan
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
import datetime as dt
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages

## Return the designated lapangan info
def show_edit_form(request, id):
    lapangan = Lapangan.objects.get(pk=id)

    ## Give hour choice and jam_buka jam_tutup lapangan 
    hour_choices = [{
        'values': '{:02d}:00:00'.format(x),
        'show':'{:02d}:00'.format(x),
        'jam_buka_selected': True if '{:02d}:00:00'.format(x) == str(lapangan.jam_buka) else False,
        'jam_tutup_selected': True if '{:02d}:00:00'.format(x) == str(lapangan.jam_tutup) else False
    }
    for x in range(0, 24)]

    context = {
        'lapangan':lapangan,
        'hour_choices':hour_choices
    }

    # The function will give the form the data needed to the update_form
    return render(request,'update_form.html',context)

    # For now the function will return the lapangan object as JSON
    # print(Jadwal.objects.filter(lapangan_id = id))
    # return HttpResponse(serializers.serialize("json", lapangan), content_type="application/json")

## Save the edited jadwal
@csrf_exempt
def edit_jadwal(request, id):
    if request.method == 'POST':
        edited_lapangan = Lapangan.objects.get(pk=id)

        ## Get the jadwal from string and convert it to datetime.time
        jam_buka = request.POST.get("jam-buka")
        jam_tutup = request.POST.get("jam-tutup")
        time_buka_hr =  jam_buka.split(':')[0]
        time_tutup_hr = jam_tutup.split(':')[0]

        ## Validate changes
        if not validate_change(edited_lapangan, time_buka_hr, time_tutup_hr) :
            return JsonResponse({
                'status':'failed',
                'message':'Tidak bisa mengedit ketersediaan lapangan karena ada jadwal yang bentrok'})
                 
        edited_lapangan.jam_buka = dt.time(int(time_buka_hr),00)
        edited_lapangan.jam_tutup = dt.time(int(time_tutup_hr),00)

        edited_lapangan.save()

    return JsonResponse({
                'status':'Success',
                'message':'Jadwal Berhasil diperbarui'},
                 status=201)
    
## Validate request if there's conflict between booked jadwal
## and new jadwal
def validate_change(lapangan, jam_buka, jam_tutup):
    jadwals = lapangan.jadwal_set.all().order_by('start').values()

    if len(jadwals)==0:
        return True

    first_jadwal = jadwals[0]
    last_jadwal = jadwals[len(jadwals)-1]

    time_buka = dt.time(int(jam_buka),00)
    time_tutup = dt.time(int(jam_tutup),00)

    ## first jadwal can't be before open time and last jadwal can't be after close time
    if first_jadwal['start'] < time_buka or last_jadwal['end'] > time_tutup:
        return False 

    return True

def show_my_lapangan(request):
    mitra = request.user

    lapangan = Lapangan.objects.filter(mitra=mitra)
    context = {
        'lapangans':lapangan,
    }
    
    return render(request, 'lapangan_page.html',context)