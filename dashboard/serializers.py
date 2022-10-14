from rest_framework import serializers
from .models import *


class account(serializers.ModelSerializer):
    class Meta:
        model=profile
        fields=['name','bio','location']
