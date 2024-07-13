from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=('movies','year','genre','rating','one_line','stars','votes','run_time','gross')