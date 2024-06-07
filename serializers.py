from rest_framework import serializers
from.models import *

class dayserializer(serializers.ModelSerializer):
    class Meta:
        models = day
        fields = "__all__"