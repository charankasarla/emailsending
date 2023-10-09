from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    to_email = serializers.EmailField()
    subject = serializers.CharField(max_length=1000)
    message = serializers.CharField()
