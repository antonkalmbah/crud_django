from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notepad

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Notepad
from .serializers import *

@api_view(['GET'])
def index(request):
    try:
        if request.method == 'GET':
            notes = Notepad.objects.all()
            serialize_note = NotepadSerializers(notes, many = True)
            # возвращает Django REST framework с API моего блокнота
            return(Response({'data': serialize_note.data}))
            # return render(request, 'notepad/index.html', {'notes': notes})
    except:
        return HttpResponse('Ошибка в функции index в файле views в приложении notepad')

def form_add(request):
    try:
        return render(request, 'notepad/create.html')
    except:
        print("Не работает form_add")


def create(request):
    try:
        if request.method == "POST":
            note = Notepad()
            note.heading = request.POST.get("heading")
            note.text = request.POST.get("text")
            note.save()
        return HttpResponseRedirect("/")

    except:
        return HttpResponse('Ошибка в функции create в файле views в приложении notepad')

def delete(request, id):
    try:
        note = Notepad.objects.get(id=id)
        note.delete()
        return HttpResponseRedirect("/")
    except:
        print('Записи не существует')

def edit(request, id):
    try:
        note = Notepad.objects.get(id=id)

        if request.method == "POST":
            note.heading = request.POST.get("heading")
            note.text = request.POST.get("text")
            note.save()

            return HttpResponseRedirect("/")
        else:
            return render(request, 'notepad/edit.html', {'note' : note})

    except:
        return HttpResponse('Ошибка в функции edit в файле views в приложении notepad')



