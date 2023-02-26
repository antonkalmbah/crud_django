from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notepad

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
            return render(request, 'notepad/edit.html', {'note' : note})

    except:
        return HttpResponse('Ошибка в функции edit в файле views в приложении notepad')