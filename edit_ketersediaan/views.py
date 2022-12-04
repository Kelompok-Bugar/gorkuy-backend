from django.shortcuts import render
from database.models import Jadwal, Lapangan
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core import serializers
import datetime as dt
from django.views.decorators.csrf import csrf_exempt

## Return the designated lapangan info
def show_edit_form(request, id):
    lapangan = Lapangan.objects.filter(pk=id)

    context = {
        'lapangan':lapangan 
    }

    # The function will give the form the data needed to the update_form
    # return render(request,'update_form.html',context)

    # For now the function will return the lapangan object as JSON
    # print(Jadwal.objects.filter(lapangan_id = id))
    return HttpResponse(serializers.serialize("json", lapangan), content_type="application/json")

## Save the edited jadwal
@csrf_exempt
def edit_jadwal(request, id):
    if request.method == 'POST':
        print('oke')
        edited_lapangan = Lapangan.objects.get(pk=id)

        ## Get the jadwal from string and convert it to datetime.time
        jam_buka = request.POST.get("jam_buka")
        jam_tutup = request.POST.get("jam_tutup")
        
        time_buka_hr =  jam_buka.split(':')[0]
        time_tutup_hr = jam_tutup.split(':')[0]

        edited_lapangan.jam_buka = dt.time(int(time_buka_hr),00)
        edited_lapangan.jam_tutup = dt.time(int(time_tutup_hr),00)

        edited_lapangan.save(['jam_buka','jam_tutup'])

    return HttpResponse(status=201)
    
