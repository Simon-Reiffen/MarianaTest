from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from fizzbuzz.models import fizzbuzz
from fizzbuzz.serializers import fizzbuzzSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import RequestContext, loader



class JSONResponse(HttpResponse):
	"""
    An HttpResponse that renders its content into JSON.  A Custome Response designed to make output cleaner
    """
	def __init__(self, data, **kwargs):
         content = JSONRenderer().render(data)
         kwargs['content_type'] = 'application/json'
         super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@api_view(['GET'])	
def get(request):
	"""
	List all fizzbuzz(s).
	"""
	
	frizz = fizzbuzz.objects.all()
	serializer = fizzbuzzSerializer(frizz, many=True)
	return JSONResponse(serializer.data)
	
@csrf_exempt	
@api_view(['GET','POST'])
#NOTE: The API view above allows for both GET and POST methods for the post function. 
#This is only for testing purposes, as most browsers only allow for GET requests from the URL, and
#I wanted to use this function as a view. In production, I'd imagine this function
#would only be called through <form action> calls, which would let you set the method to POST.
#In this case, you wouldn't 		
def post(request, pk):
	"""
	Add a fizzbuzz
	"""
	
	frizz = fizzbuzz(message=pk, useragent =request.META.get('HTTP_USER_AGENT', ''))
	frizz.save()
	return HttpResponse("The fizzbuzz was created with the message: " + pk) 
	#Note: I decided to return an HttpResponse response just to let the user know that the post was successful.
	#It can be removed/replaced without impacting the functionality of this code.
@api_view(['GET'])		
def getI(request, pk):
	"""
	Retrieve a fizzbuzz.
	"""
	try:
		frizz = fizzbuzz.objects.get(pk=pk)
		serializer = fizzbuzzSerializer(frizz)
		return JSONResponse(serializer.data)	
	except fizzbuzz.DoesNotExist:
		return HttpResponse("Sorry, that fizzbuzz does not exist")
@csrf_exempt			
@api_view(['GET', 'POST'])		
def swiss(request,format = None, **pk):
	"""
	Retrieve, update or delete a fizzbuzz. Called swiss because the same view can do multiple things
	"""
	 

	if (len(pk) == 0): #If there is no data to search for or post, then we GET everything
		if request.method == 'GET':
			frizz = fizzbuzz.objects.all()
			serializer = fizzbuzzSerializer(frizz, many=True)
			return JSONResponse(serializer.data)
	else:
	
		if request.method == 'GET':
			
			try:
				frizz = fizzbuzz.objects.get(pk=pk['pk'])
				serializer = fizzbuzzSerializer(frizz)
				return JSONResponse(serializer.data)

			except fizzbuzz.DoesNotExist:
				return HttpResponse(status=404)
			
		elif request.method == 'POST':
			frizze = fizzbuzz(message=pk['pk'], useragent =request.META.get('HTTP_USER_AGENT', ''))
			frizze.save()
			
			return HttpResponse("The fizzbuzz was created with the message: " + pk['pk'])
	return HttpResponse("We're sorry we could not provide the service you wanted")
	#NOTE: This should never come up, unless something has gone wrong (such a POST attempt with no data to post)

def demo(request, **pk):
	"""
	allows for in browser access of the SWISS method. Note: It expects an argument
	"""
	if (len(pk) == 0):
		text = " "
		
	else:
		text = pk['pk']
		
	template = loader.get_template('fizzbuzz/demo.html')
	

	context = RequestContext(request, {'text':text})
	return HttpResponse(template.render(context))
	
			
