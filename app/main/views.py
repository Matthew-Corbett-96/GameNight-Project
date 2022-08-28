from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Test View
def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request=request, template_name='main/index.html')
