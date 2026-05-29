from django.http import HttpResponse


def first(request):
    return HttpResponse("Hello World")

def second(request):
    return HttpResponse("Hello django I am excited to learn you")

def user(request):
    return HttpResponse("Hello dJango today i learned about django")

