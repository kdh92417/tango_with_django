from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')


def favorite(request):
    favorite_dict = {'my_favorite' : "영화보기, 자전거 타기, 라이딩 하기, 송도 걷기, 노을 보기, 책보기, 음악 듣기"}

    return render(request, 'rango/portfolio.html' ,context=favorite_dict)