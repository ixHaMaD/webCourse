from django.shortcuts import render


def index(request):
    #renders the appropriate template for this request
    return render(request, 'bookmodule/index.html') #the index.html file must be in the templates

def index2(request):

    return render(request, 'bookmodule/index2.html')

def index3(request, val):
    return render(request, 'bookmodule/index3.html')