#https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/
from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['name', 'detail']
