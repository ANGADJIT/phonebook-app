from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phonenumber', 'contact_type']


class ContactSearchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=False)
