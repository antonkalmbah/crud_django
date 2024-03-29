from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .serializers import NotepadSerializers
from .models import Notepad
from rest_framework import viewsets


class NotepadViewSets(viewsets.ModelViewSet):
    queryset = Notepad.objects.all()
    serializer_class = NotepadSerializers


def index(request):
    try:
        if request.method == 'GET':
            notes = Notepad.objects.all()
            # возвращает html-страничку из templates самого плагина
            return render(request, 'notepad/list.html', {'notes': notes})
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
        return HttpResponse('Записи не существует')


def edit(request, id):
    try:
        note = Notepad.objects.get(id=id)
        if request.method == "POST":
            note.heading = request.POST.get("heading")
            note.text = request.POST.get("text")
            note.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, 'notepad/edit.html', {'note': note})
    except:
        return HttpResponse('Ошибка в функции edit в файле views в приложении notepad')
    
def sql(request):
    sql_note = Notepad.objects.raw('SELECT * FROM notepad_notepad')
    
    for note in sql_note:
        print(str(note.id) + note.heading + note.text)
        
    return HttpResponse('all')