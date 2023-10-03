from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = """<h1>"Изучаем djsngo"</h1>
            <strong>Автор</strong>: <i>Отцовский А.А.</i>
            """
    return HttpResponse(text)
