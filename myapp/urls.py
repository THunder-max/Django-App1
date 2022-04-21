from django.urls import  path 
from . import views

urlpatterns = [
    #view examples
    path('',views.myfunctioncall,name='Index'),
    path('about',views.myfunctionabout,name='About'),
    path('add/<int:a>/<int:b>',views.myfunctionadd,name='add'),
    path('intro/<str:name>/<int:age>',views.intro,name='intro'),
    #main views
    path('index',views.myindex,name='index'),
    path('secondpage',views.mysecondpage,name='secondpage'),
    path('thirdpage',views.mythirdpage,name='thirdpage'),

]