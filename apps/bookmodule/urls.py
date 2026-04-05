
from django.urls import path, include
from apps.bookmodule import views


urlpatterns = [
    #path('arguments in URL', views.function_name, name=???)
    path('', views.home_page, name='home_page'), #in views.py we must add the index function
    path('2', views.second_page, name='second_page'),
    path('book/<val>', views.third_page, name='third_page'),
    path('forth',views.forth_page, name='forth_page')
]


