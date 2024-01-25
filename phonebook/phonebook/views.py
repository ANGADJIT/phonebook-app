from rest_framework.views import APIView
from rest_framework.request import Request
from .serializers import ContactSerializer, ContactSearchSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Contact
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView


class AddContactView(APIView):

    def post(self, request: Request):
        data = request.data
        contact_serializer = ContactSerializer(data=data)

        if contact_serializer.is_valid():
            contact_serializer.save()

            return Response(data=contact_serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(data={'error': contact_serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class ListContactsView(ListAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class UpdateContactView(RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'


class SearchContactView(ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        queryset = Contact.objects.all()
        search_serializer = ContactSearchSerializer(
            data=self.request.query_params)

        if search_serializer.is_valid():
            name_value = search_serializer.validated_data.get('name')
            if name_value:
                queryset = queryset.filter(name__icontains=name_value)

        return queryset
