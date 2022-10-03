from dataclasses import fields
from .models import Krosovka
from rest_framework import serializers

class KrosovkaAPI(serializers.ModelSerializer):
    class Meta:
        model = Krosovka
        fields = '__all__'
