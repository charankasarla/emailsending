from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmailSerializer
from django.core.mail import send_mail
# Create your views here.


class EmailSendView(APIView):
    serializer_class = EmailSerializer
    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            to_email = serializer.validated_data.get('to_email')
            subject = serializer.validated_data.get('subject')
            message = serializer.validated_data.get('message')

            send_mail(subject,message,'shivasaicharankasarla03@gmail.com',[to_email])
            return Response({'message':'Email Sent Sucessfully'},status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
