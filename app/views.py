from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def calc(request):
    num1 = int(request.POST.get('num1'))
    num2 = int(request.POST.get('num2'))
    input = ''
    
    # if 'num' in request.POST:
    #     val = request.POST.get('num')
    #     print(val)
    #     input = input+val
    #     return render(request, 'home.html', {'input' : input})


    if 'value_add' == request.POST.get('name_add'):
        result = num1 + num2
        return render(request, 'home.html', {'result' : result})
    elif 'value_sub' == request.POST.get('name_sub'):
        result = num1 - num2
        return render(request, 'home.html', {'result' : result})
    elif 'value_mult' == request.POST.get('name_mult'):
        result = num1 * num2
        return render(request, 'home.html', {'result' : result})
    else:
        result = num1/num2
        return render(request, 'home.html', {'result' : result})