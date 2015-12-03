from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from fizzbuzz.models import fizzbuzz
from fizzbuzz.serializers import fizzbuzzSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import detail_route
from django.shortcuts import get_object_or_404
from rest_framework import viewsets




class JSONResponse(HttpResponse):
	"""
    An HttpResponse that renders its content into JSON.  A Custome Response designed to make output cleaner
    """
	def __init__(self, data, **kwargs):
         content = JSONRenderer().render(data)
         kwargs['content_type'] = 'application/json'
         super(JSONResponse, self).__init__(content, **kwargs)
		 

class fizzbuzzViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and creating fizzbuzz instances.
    """


    serializer_class = fizzbuzzSerializer
    queryset = fizzbuzz.objects.all()

    def list(self, request):
		#Retrieves all of the fizzbuzzes
        queryset = fizzbuzz.objects.all()
        serializer = fizzbuzzSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
		#Retrieves a specific fizzbuzz
        queryset = fizzbuzz.objects.all()	
        frizz = get_object_or_404(queryset, pk=pk)
        serializer = fizzbuzzSerializer(frizz)
        return Response(serializer.data)
    def create(self, request):
		#creates a fizzbuzz
        data = JSONParser().parse(request)
        frizz = fizzbuzz(message=data['message'], useragent =request.META.get('HTTP_USER_AGENT', ''))
        frizz.save()
        serializer = fizzbuzzSerializer(frizz)
        return JSONResponse(serializer.data)	
	
