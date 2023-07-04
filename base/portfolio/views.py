from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics, permissions, authentication
from .models import Projects
from .serializers import ProjectsSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ProjectUpdateAPIView(generics.UpdateAPIView):
    """
    Update a specific project.

    ---
    # Request Body
    - title: Title of the project (string)
    - content: Content of the project (string)

    # Response
    - id: ID of the updated project (integer)
    - title: Title of the updated project (string)
    - content: Content of the updated project (string)
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

project_update_view = ProjectUpdateAPIView.as_view()

class ProjectDeleteAPIView(generics.DestroyAPIView):
    """
    Delete a specific project.

    ---
    # Request
    - pk: ID of the project to be deleted (integer)
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

project_delete_view = ProjectDeleteAPIView.as_view()

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    """
    List and create projects.

    ---
    # Request Body (Create)
    - title: Title of the project (string)
    - content: Content of the project (string)

    # Response (List)
    - id: ID of the project (integer)
    - title: Title of the project (string)
    - content: Content of the project (string)
    """
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
        serializer.save()

project_list_create_view = ProjectListCreateAPIView.as_view()

class ProjectListAPIView(generics.ListAPIView):
    """
    List all projects.

    ---
    # Response
    - id: ID of the project (integer)
    - title: Title of the project (string)
    - content: Content of the project (string)
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

project_list_view = ProjectListAPIView.as_view()

@api_view(["GET", "POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def project_alt_view(request, pk=None, *args, **kwargs):
    """
    Alternative project view.

    ---
    # Request (GET)
    - pk: ID of the project to retrieve (integer)

    # Response (GET)
    - id: ID of the project (integer)
    - title: Title of the project (string)
    - content: Content of the project (string)

    # Request (POST)
    - title: Title of the project (string)
    - content: Content of the project (string)

    # Response (POST)
    - id: ID of the created project (integer)
    - title: Title of the created project (string)
    - content: Content of the created project (string)
    """
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
