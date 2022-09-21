from django.shortcuts import render
from .models import Quiz
# Create your views here.
#下記のコードは追加
def monndai_show(request):
    question = Quiz.objects.order_by('?').first()
    context = {'question': question}
    return render(request,'templates.html',context)

def move_to_seikaipage(request):
    return render(request, 'seikaipage.html')

def move_to_fuseikaipage(request):
    return render(request, 'fuseikaipage.html')

def monndai2_show(request):
    return render(request,'monndai2.html')