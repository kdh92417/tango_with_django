from django.conf.urls import url
from django.urls      import path

from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^portfolio/', views.favorite, name='favorite'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category')
]
