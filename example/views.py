# example/views.py
from django.http import response

def index(request):

    return response(request,'index.html')