from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from rest_framework.response import Response
from django.forms import  model_to_dict
from rest_framework.decorators import api_view
from portfolio.models import Projects
from portfolio.serializers import ProjectsSerializer
# Create your views here.
@api_view(['GET'])
def api_home(request, *args, **kwargs):
  """
  DRF API VIEW
  """
  # instance = Projects.objects.all().order_by("?").first()
  # # projects = Projects.objects.all().order_by("?").first()
  # data = {}
  # if instance:
  #   # data = model_to_dict(projects,fields=['id','title','my_fixed_repo'])
  #   data = ProjectsSerializer(instance).data
  #   # data['title'] = projects.title
  #   # data['content'] = projects.content
  #   # data['repository'] = projects.repository
  serilizer = ProjectsSerializer(data=request.data)
  if serilizer.is_valid(raise_exception=True):
    print(serilizer.data)
    return Response(serilizer.data)
  return Response({"Invalid":"This is not good data"},status=400)