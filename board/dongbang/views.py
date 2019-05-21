from django.shortcuts import render, redirect
from .models import Message

# Create your views here.
def board(r):
    messages = Message.objects
    return render(r, 'board.html',{'messages':messages})

def submit(r):
    m = Message()
    m.content = r.GET['words']
    m.date = r.GET['date']
    m.writer = r.GET['writer']
    m.save()
    return redirect('/')

def search(r):
    key = r.GET['keyword']
    messages = Message.objects
    if key in messages:
        result = '있'
    else:
        result = '없'
    return render(r, 'search.html',{'key':key,'result':result,'messages':messages})

