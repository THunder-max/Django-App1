from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def myfunctioncall(request):
    return HttpResponse('Index')

def myfunctionabout(request):
    return HttpResponse('About page')

def myfunctionadd(request,a,b):
    return HttpResponse(a+b)

#json response
def intro(request,name,age):
    mydictionary = {
        'name' : name ,
        'age' : age
    }
    return JsonResponse(mydictionary)

#template

def myindex(request):
    return render(request, 'index.htm')

def mysecondpage(request):
    return render(request, 'secondpage.htm') 


def mythirdpage(request):
    var = 'hello world'
    greeting = 'how are you'
    fruits = ["Apple", "Mango", "Pear"]
    num1 , num2 = 7 , 5
    ans = num1 > num2
    # print(ans)
    mydictionary = {
        'var' : var,
        'msg' : greeting,
        'myfruits' : fruits,
        'num1': num1,
        'num2':num2,
        'ans':ans
    }
    return render(request, 'thirdpage.htm',context=mydictionary)