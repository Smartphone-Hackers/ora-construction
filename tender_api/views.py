from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from tender import models
from tender_api import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def tender_lists(request):
    if request.method == "GET":
        tender = models.TenderDetails.objects.all()
        serializer = serializers.TenderDeatailSerializer(tender, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def tender_list(request, pk):
    if request.method == "GET":
        tender = models.TenderDetails.objects.get(tender_id=pk)
        serializer = serializers.TenderDeatailSerializer(tender)
        return Response(serializer.data)
