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
from rest_framework import serializers




def main():
	print "HEllo"
main()