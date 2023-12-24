from rest_framework import serializers
from.models import *

class CategotySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoty
        fields = '__all__'

class Bookserializer(serializers.ModelSerializer):
    category = CategotySerializer()  # Use CategotySerializer for the category field

    class Meta:
        model = Book
        fields = '__all__'