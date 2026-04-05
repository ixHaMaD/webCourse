from django.shortcuts import render
name = 'Hamad Mohammed'

def home_page(request):
    #renders the appropriate template for this request
    return render(request, 'bookmodule/index.html', {'var1':name}) #the index.html file must be in the templates

def second_page(request):

    return render(request, 'bookmodule/index2.html')

def third_page(request, val):
    return render(request, 'bookmodule/index3.html')

def forth_page(request):
    return render(request, 'bookmodule/index4.html')