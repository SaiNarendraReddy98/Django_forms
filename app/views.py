from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.



def insert_topic(request):
    TFO = Topicforms()
    d={'TFO':TFO}
    if request.method == 'POST':
        TOD = Topicforms(request.POST)
        if TOD.is_valid():
            TN = TOD.cleaned_data['topic_name']
            TO = Topic.objects.get_or_create(topic_name=TN)[0]
            TO.save()
            return HttpResponse (str(TOD.cleaned_data))
        
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_topic.html',d)




def insert_webpage(request):
    WFO = Webpageforms()
    d={'WFO':WFO}
    if request.method == 'POST':
        WOD = Webpageforms(request.POST)
        if WOD.is_valid():
            tn=WOD.cleaned_data['topic_name']
            TO = Topic.objects.get(topic_name=tn)
            n=WOD.cleaned_data['name']
            u=WOD.cleaned_data['url']
            e=WOD.cleaned_data['email']
            WO = Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()
            return HttpResponse(str(WOD.cleaned_data))
        else:
            return HttpResponse('invalid data')
    

    return render(request,'insert_webpage.html',d)





def insert_accessrecord(request):
    AFO = Accessrecordforms()
    d={'AFO':AFO}
    if request.method == 'POST':
        AOD = Accessrecordforms(request.POST)
        if AOD.is_valid():
            n = AOD.cleaned_data['name']
            WO = Webpage.objects.get(pk=n)
            d = AOD.cleaned_data['date']
            au = AOD.cleaned_data['author']
            AO = Accessrecord.objects.get_or_create(name=WO,date=d,author=au)[0]
            AO.save()
            return HttpResponse(str(AOD.cleaned_data))
        else:
            return HttpResponse('invalid data')

    
    return render(request,'insert_accessrecord.html',d)