from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *

# Create your views here.

def dj_forms(request):
    NO = NameForm()
    d={'form':NO}

    if request.method == 'POST':
        NOB = NameForm(request.POST)
        if NOB.is_valid():
            sn=NOB.cleaned_data['Sname']
            sag=NOB.cleaned_data['Sage']
            spd=NOB.cleaned_data['Spassword']
            sgn=NOB.cleaned_data['Sgender']
            cs=NOB.cleaned_data['Courses']
            sad=NOB.cleaned_data['Saddress']

            SOB=School.objects.get_or_create(sname=sn,sage=sag,spawd=spd,sgen=sgn,course=cs,address=sad)[0]
            SOB.save()
            QLSO=School.objects.all()
            d1={'data':QLSO}
            return render(request,'display_data.html',d1)

            #return HttpResponse(str(NOB.cleaned_data))
            #return HttpResponse(NOB.cleaned_data['Sname'])
        else:
            return HttpResponse('invalid data')


    return render(request,'dj_forms.html',d)
