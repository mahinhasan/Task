from django.shortcuts import render
from django.http import HttpResponse
from .models import Ancient
from .serializers import AncientSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

def home(request):
    anc = Ancient.objects.all()
    serializer = AncientSerializer(anc,many=True)
    json_renderer = JSONRenderer()
    json_data = json_renderer.render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')



def ancient_details(request,pk):
    anc = Ancient.objects.get(id=pk)
    serial = AncientSerializer(anc)
    json_renderer = JSONRenderer()
    json_data = json_renderer.render(serial.data)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def ancient_create(request):
    if request.method=='POST':
        json_data = request.body
        print("Get it",json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        json_parser = JSONParser()
        json_renderer = JSONRenderer()
        pydata = json_parser.parse(stream)
        serializer = AncientSerializer(data=pydata)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json_data,content_type='application/json')
        return HttpResponse("Done")
    
    