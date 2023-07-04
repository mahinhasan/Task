from rest_framework import serializers
from .models import Projects


class ProjectsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Projects
        fields = ("title","content","my_fixed_repo")