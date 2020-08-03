from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    FirstName = serializers.CharField(max_length=255)
    LastName = serializers.CharField(max_length=255)
    BirthDate = serializers.DateField()
    RegistrationDate = serializers.DateField()
