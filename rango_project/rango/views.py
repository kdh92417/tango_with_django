from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories' : category_list}

    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')


def favorite(request):
    favorite_dict = {'my_favorite' : "영화보기, 자전거 타기, 라이딩 하기, 송도 걷기, 노을 보기, 책보기, 음악 듣기"}

    return render(request, 'rango/portfolio.html' ,context=favorite_dict)
