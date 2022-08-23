from django.shortcuts import render
from django.http import HttpResponse

# Test View
def index(request) -> HttpResponse:
    if request:
        return HttpResponse("Hello, world. You're at the polls index.")
    else:
        return HttpResponse(content="Meow Meow cats")
