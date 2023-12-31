from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
# Create your views here.
author = {
    "Имя": "Александр",
    "Отчество": "Андреевич",
    "Фамилия": "Отцовский",
    "телефон": "8-000-000-00-00",
    "email": "coresh@mail.ru"

}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def index(request):
    # text = """<h1>"Изучаем django"</h1>
    #           <strong>Автор</strong>: <i>Отцовский А.А.</i>
    #        """
    # return HttpResponse(text)
    context = {
        "name": "Отцовский А.А.",
        "email": "my_mail@example.com",
            }
    return render(request, "index.html", context)

def about(request):
    result = f"""
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(result)

# /item/1
# /item/2
# /item/3

def get_item(request, id):
    """ По указанному id возвращает имя и количество """
    for item in items:
        if item["id"] == id:
            result = f"""
            <h2>Имя: {item["name"]} </h2>
            <p>Количество: {item["quantity"]} </p>
            <p><a href="/items"> Назад к списку товаров </a></p>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f'Item with id={id} not found')


# <ol>
#     <li> ... </li>
#     <li> ... </li>
#     <li> ... </li>
#     <li> ... </li>
# </ol>
def items_list(request):
    result = "<h2>Список товаров</h2><ol>"
    for item in items:
        result += f"""<li><a href="/item/{item['id']}">{item['name']}</a></li>"""
    result += '</ol>'
    return HttpResponse(result)

def countrie_list(request):
    return render(request, "countries.html")

def Australia(request):
    return render(request, "Australia.html")

def Austria(request):
    return render(request, "Austria.html")

def Bahamas(request):
    return render(request, "Bahamas.html")