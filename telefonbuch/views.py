from django.shortcuts import render
from django.http import HttpResponse
from .models import TelefonbuchEintrag
# Create your views here.

def hello(request):
    return HttpResponse("Hello Sir or Madam")

def eintraege(request):
    eintraege = TelefonbuchEintrag.objects.all()
    return render(request,'eintraege.html',context= {'eintraege': eintraege})
