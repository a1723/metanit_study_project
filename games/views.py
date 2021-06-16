from django.shortcuts import render
from django.http import *
from django.template.response import TemplateResponse

def index(request):
    langs = ["English", "German", "French", "Spanish", "Chinese"]
    return render(request, "index.html", context={"langs": langs})


"""def index(request):
    header = "Personal Data"                    # обычная переменная
    langs = ["English", "German", "Spanish"]    # массив
    user ={"name" : "Tom", "age" : 23}          # словарь
    addr = ("Абрикосовая", 23, 45)              # кортеж
 
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return TemplateResponse(request,  "index.html", data)"""
 

def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Product № {0}  Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "qweqe")
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)


def m304(request):
    return HttpResponseNotModified()
 

def m400(request):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")


def m403(request):
    return HttpResponseForbidden("<h2>Forbidden</h2>")


def m404(request):
    return HttpResponseNotFound()


def m405(request):
    return HttpResponseNotAllowed("<h2>Method is not allowed</h2>")


def m410(request):
    return HttpResponseGone("<h2>Content is no longer here</h2>")


def m500(request):
    return HttpResponseServerError("<h2>Something is wrong</h2>")
