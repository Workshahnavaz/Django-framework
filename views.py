from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def myfund(request):
    return Response({"status":200,"message":"done"})

# Create your views here.
