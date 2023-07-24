from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics, permissions, authentication
from .models import Projects
from .serializers import ProjectsSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Projects
from .serializers import ProjectsSerializer
from django.core.files.storage import default_storage
import os
from django.http import HttpResponseNotFound, FileResponse

@csrf_exempt
def myProjects(request, id=None):
    if request.method == 'GET':
        projects = Projects.objects.all()
        projects_serializer = ProjectsSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe=False)

    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        project_serializer = ProjectsSerializer(data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse("Project added successfully", safe=False, status=201)
        return JsonResponse(project_serializer.errors, safe=False, status=400)

    elif request.method == 'PUT':
        if id is not None:
            project_data = JSONParser().parse(request)
            try:
                project = Projects.objects.get(id=id)
            except Projects.DoesNotExist:
                return JsonResponse("Project not found", safe=False, status=404)

            project_serializer = ProjectsSerializer(project, data=project_data)
            if project_serializer.is_valid():
                project_serializer.save()
                return JsonResponse("Project updated successfully", safe=False)
            return JsonResponse(project_serializer.errors, safe=False, status=400)
        else:
            return JsonResponse("Project ID is missing in request", safe=False, status=400)

    elif request.method == 'DELETE':
        if id is not None:
            try:
                project = Projects.objects.get(id=id)
                project.delete()
                return JsonResponse("Project deleted successfully", safe=False)
            except Projects.DoesNotExist:
                return JsonResponse("Project not found", safe=False, status=404)
        else:
            return JsonResponse("Project ID is missing in request", safe=False, status=400)

    return JsonResponse("Method not allowed", safe=False, status=405)


@csrf_exempt
def saveFile(request):
    file = request.FILES['uploadedFile']
    filename = default_storage.save(file.name,file)
    return JsonResponse(filename,safe=False)

def getImage(request, filename):
    # Assuming you have a specific directory where the uploaded files are saved.
    # Replace 'path/to/your/directory/' with the actual directory path where the files are stored.
    upload_dir = 'media/'

    # Create the full file path.
    file_path = os.path.join(upload_dir, 'unnamed.jpg')

    # Check if the file exists.
    if os.path.exists(file_path):
        # Serve the file using FileResponse.
        return FileResponse(open(file_path, 'rb'), content_type='image/jpeg')
    else:
        # Return a 404 Not Found response if the file does not exist.
        return HttpResponseNotFound("Image not found.")


# class ProjectUpdateAPIView(generics.UpdateAPIView):
#     """
#     Update a specific project.

#     ---
#     # Request Body
#     - title: Title of the project (string)
#     - content: Content of the project (string)

#     # Response
#     - id: ID of the updated project (integer)
#     - title: Title of the updated project (string)
#     - content: Content of the updated project (string)
#     """
#     queryset = Projects.objects.all()
#     serializer_class = ProjectsSerializer
#     lookup_field = 'pk'

#     def perform_update(self, serializer):
#         instance = serializer.save()
#         if not instance.content:
#             instance.content = instance.title

# project_update_view = ProjectUpdateAPIView.as_view()

# class ProjectDeleteAPIView(generics.DestroyAPIView):
#     """
#     Delete a specific project.

#     ---
#     # Request
#     - pk: ID of the project to be deleted (integer)
#     """
#     queryset = Projects.objects.all()
#     serializer_class = ProjectsSerializer
#     lookup_field = 'pk'

#     def perform_destroy(self, instance):
#         return super().perform_destroy(instance)

# project_delete_view = ProjectDeleteAPIView.as_view()

# class ProjectListCreateAPIView(generics.ListCreateAPIView):
#     """
#     List and create projects.

#     ---
#     # Request Body (Create)
#     - title: Title of the project (string)
#     - content: Content of the project (string)

#     # Response (List)
#     - id: ID of the project (integer)
#     - title: Title of the project (string)
#     - content: Content of the project (string)
#     """
#     queryset = Projects.objects.all()
#     serializer_class = ProjectsSerializer
#     authentication_classes = [authentication.SessionAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         title = serializer.validated_data.get("title")
#         content = serializer.validated_data.get("content") or None
#         if content is None:
#             content = title
#         serializer.save(content=content)
#         serializer.save()

# project_list_create_view = ProjectListCreateAPIView.as_view()

# class ProjectListAPIView(generics.ListAPIView):
#     """
#     List all projects.

#     ---
#     # Response
#     - id: ID of the project (integer)
#     - title: Title of the project (string)
#     - content: Content of the project (string)
#     """
#     queryset = Projects.objects.all()
#     serializer_class = ProjectsSerializer

# project_list_view = ProjectListAPIView.as_view()

# @api_view(["GET", "POST"])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# def project_alt_view(request, pk=None, *args, **kwargs):
#     """
#     Alternative project view.

#     ---
#     # Request (GET)
#     - pk: ID of the project to retrieve (integer)

#     # Response (GET)
#     - id: ID of the project (integer)
#     - title: Title of the project (string)
#     - content: Content of the project (string)

#     # Request (POST)
#     - title: Title of the project (string)
#     - content: Content of the project (string)

#     # Response (POST)
#     - id: ID of the created project (integer)
#     - title: Title of the created project (string)
#     - content: Content of the created project (string)
#     """
#     method = request.method
#     if method == "GET":
#         if pk is not None:
#             obj = get_object_or_404(Projects, pk=pk)
#             data = ProjectsSerializer(obj, many=False).data
#             return Response(data)
#         qr = Projects.objects.all()
#         data = ProjectsSerializer(qr, many=True).data
#         return Response(data)
#     if method == "POST":
#         serializer = ProjectsSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get("title")
#             content = serializer.validated_data.get("content") or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"Invalid": "This is not good data"}, status=400)
