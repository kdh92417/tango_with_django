# 프로젝트에 startapps 명령어로 생성되지 않은 파일에서 장고에 등록된 모델이나 함수를 사용할 때 다음과 같은 에러가발생하여 밑에 밑으 코드추가
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rango_project.settings")

import django
django.setup()

from rango.models import Category, Page

def populate():
    python_pages = [
        {
            "title": "Official Python Tutorial",
            "url":"http://docs.python.org/2/tutorial/"
        },
        {
            "title":"How to Think like a Computer Scientist",
            "url":"http://www.greenteapress.com/thinkpython/"
        },
        {
            "title":"Learn Python in 10 Minutes",
            "url":"http://www.korokithakis.net/tutorials/python/"
        }
    ]

    django_pages = [
        {
            "title":"Official Django Tutorial",
            "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"
        },
        {
            "title":"Django Rocks",
            "url":"http://www.djangorocks.com/"
        },
        {
            "title":"How to Tango with Django",
            "url":"http://www.tangowithdjango.com/"
        }
    ]

    other_pages = [
        {
            "title":"Official Django Tutorial",
            "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"
        },
        {
            "title":"Django Rocks",
            "url":"http://www.djangorocks.com/"
        },
        {
            "title":"How to Tango with Django",
            "url":"http://www.tangowithdjango.com/"
        }
    ]

    cats = {
        "Python":
            {
                "pages": python_pages,
                "likes" : 128,
                "views" : 64
            },
        "Django":
            {
                "pages": django_pages,
                "views" : 64,
                "likes" : 32
            },
        "Other Frameworks":
            {
                "pages": other_pages,
                "views" : 32,
                "likes" : 16
            }
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])    # cat : Python      52
        for p in cat_data["pages"]: # python_ages {}
            add_page(c, p["title"], p["url"])

    # Print out the categories we have added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0): # python, title, url
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views, likes):  # Python
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]    # Category name이 Python인 데이터 생성
    c.save()    # 저장
    return c


# Start execution here !
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()