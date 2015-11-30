from rest_framework import serializers
from fizzbuzz.models import fizzbuzz

class fizzbuzzSerializer(serializers.ModelSerializer):
    class Meta:
        model = fizzbuzz
        fields = ('id','useragent','message','created' )
  
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
