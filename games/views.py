from django.shortcuts import render
from django.http import *

def index(request):
    return HttpResponse("Index")
 
def about(request):
    return HttpResponse("About")
 
def contact(request):
    return HttpResponseRedirect("/about")
 
def details(request):
    return HttpResponsePermanentRedirect("/")


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
