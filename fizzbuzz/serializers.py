from rest_framework import serializers
from fizzbuzz.models import fizzbuzz
from django.db import models

class fizzbuzzSerializer(serializers.ModelSerializer):

    creation_date = serializers.DateField(source='created', required=True)
    fizzbuzz_id = serializers.IntegerField(source='id', required=True)


    class Meta:
        model = fizzbuzz
        fields = ('fizzbuzz_id','useragent','message','creation_date' )

    def create(self, validated_data):
        """
        Create and return a new `fizzbuzz` instance, given the validated data.
        """
        return fizzbuzz.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `fizzbuzz` instance, given the validated data.
        """
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance
