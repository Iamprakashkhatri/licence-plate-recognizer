
from django.http import HttpResponse
from django.shortcuts import render
from .Main import Main
from .Main import DetectChars

def home(request):
    return render(request, 'home.html')
def detail(request):
    return render(request,'results.html')

    
def result_view(request):
    file = request.FILES.get('myfile')
    # file = request.FILES.get('myfile')
    textt = request.FILES.get('mytext')
    texty = request.FILES.get('mytexty')
    
   
    result = Main.main(file,textt,texty)
    result2 =DetectChars.loadKNNDataAndTrainKNN(textt,texty) 
    context = {
        'total': result
    }
    return render(request, 'home.html', context)
