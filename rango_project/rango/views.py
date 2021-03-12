from django.shortcuts import render
from django.http      import HttpResponse
from rango.models     import (
    Category,
    Page
)

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories' : category_list}

    return render(request, 'rango/index.html', context_dict)


def about(request):
    return render(request, 'rango/about.html')


def favorite(request):
    favorite_dict = {'my_favorite' : "영화보기, 자전거 타기, 라이딩 하기, 송도 걷기, 노을 보기, 책보기, 음악 듣기"}

    return render(request, 'rango/portfolio.html' ,context=favorite_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception
        category = Category.objects.get(slug=category_name_slug).order_by('-views')

        # Retrieve all of the associated pages.
        # note that filter() will return a list of page objets or an empty list
        pages = Page.objects.order_by('-likes')

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages

        # We also add the category object from the database to the context dictionary
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)
