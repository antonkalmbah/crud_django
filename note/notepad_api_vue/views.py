from django.shortcuts import render
from .models import Notepad
from .serializers import NotepadSerializers
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class IndexViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    notes = Notepad.objects.all()
    # возвращает Django REST framework с API
    serialize_note = NotepadSerializers
