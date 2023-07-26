from rest_framework import serializers
from .models import Projects,Contact


class ProjectsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Projects
        fields = ("title","content","repository")

class ContactSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Contact
        fields = ("name","content","email")
 