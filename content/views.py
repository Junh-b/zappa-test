from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contents
from .serializers import ContentsSerializer
from rest_framework.parsers import JSONParser

# Create your views here.


@csrf_exempt
def content(request, pk=None):
    # 이게 queryset 만드는거구나. pk == pk조건 달아달라는거임.

    if request.method == "GET":
        obj = Contents.objects.get(pk=pk)
        serializer = ContentsSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ContentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def contents_list(request):
    if request.method == "GET":
        query_set = Contents.objects.all()
        serializer = ContentsSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
