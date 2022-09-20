from django.shortcuts import render

# Create your views here.
#下記のコードは追加
def monndai_show(request):
    return render(request,'monndai.html') 

def move_to_seikaipage(request):
    'monndai2_show'
    return render(request, 'seikaipage.html')

def move_to_fuseikaipage(request):
    return render(request, 'fuseikaipage.html')

def monndai2_show(request):
    return render(request,'monndai2.html')