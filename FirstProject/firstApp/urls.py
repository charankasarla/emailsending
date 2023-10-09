from django.urls import path
from . import views

urlpatterns = [
    path('send_email/',views.EmailSendView.as_view(),name='send_email'),

]
