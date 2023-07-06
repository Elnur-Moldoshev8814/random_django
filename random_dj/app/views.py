from django.shortcuts import HttpResponse

from random import randint

def _random(request, num):
    return HttpResponse(randint(1, num))

def palindrom(request, text):
    if text == text[::-1]:
        answer = "it's palindrom, nigger"
    else:
        answer = "it isn't palindrom, nigger"
    return HttpResponse(answer)
