from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework import generics,mixins,permissions,authentication
from .models import Projects
from .serializers import ProjectsSerializer
from rest_framework.decorators import api_view,authentication_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.


# class ProjectDetailAPIView(generics.RetrieveAPIView):
#     queryset = Projects.objects.all()
#     serializer_class = ProjectsSerializer


# project_detail_view = ProjectDetailAPIView.as_view()




class ProjectUpdateAPIView(generics.UpdateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content :
            instance.content = instance.title
            
        


project_update_view = ProjectUpdateAPIView.as_view()



class ProjectDeleteAPIView(generics.DestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

project_delete_view = ProjectDeleteAPIView.as_view()


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)
        print(serializer.validated_data)
        serializer.save()


project_list_create_view = ProjectListCreateAPIView.as_view()


class ProjectListAPIView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


project_list_view = ProjectListAPIView.as_view()


@api_view(["GET", "POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def project_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Projects, pk=pk)
            data = ProjectsSerializer(obj, many=False).data
            return Response(data)
        qr = Projects.objects.all()
        data = ProjectsSerializer(qr, many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Invalid": "This is not good data"}, status=400)
