from django.shortcuts import render
from django.http import *
from django.template.response import TemplateResponse
from .forms import UserForm
from .models import Person


# получение данных из бд
def index(request):
    people = Person.objects.all
    return render(request, "index.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных в бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseRedirect("<h2>Person not found</h2>")


"""def index(request):
    userform = UserForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = request.POST.get("name")
            age = request.POST.get("age")
            email = request.POST.get("email")
            return HttpResponse("<h2>Hello, {0}. </br> Your age is {1} and ur email is {2}</h2>".format(name, age, email))
    return render(request, "index.html", {"form": userform})
"""
"""def index(request):
    header = "Personal Data"                    # обычная переменная
    langs = ["English", "German", "Spanish"]    # массив
    user ={"name" : "Tom", "age" : 23}          # словарь
    addr = ("Абрикосовая", 23, 45)              # кортеж
 
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return TemplateResponse(request,  "index.html", data)"""
 
