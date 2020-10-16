from rest_framework import serializers
from tender import models

class TenderDeatailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TenderDetails
        fields = "__all__"
        depth = 1