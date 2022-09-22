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

def move_to_AddText(request):
    return render(request,'AddText.html')

# #下記はtodoを参考にした
# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
# from django.views.generic import CreateView

from django.urls import reverse_lazy

from .models import Quiz

# # class QuizList(ListView):
# #     model = Quiz
# #     context_object_name = "tasks"


# # class QuizDetail(DetailView):
# #     model = Quiz
# #     context_object_name = "task"

class TodoCreate(CreateView):
    model = Quiz
    fields = "__all__"
    success_url = reverse_lazy("list")

from django.views.generic import ListView #追加

from .models import Quiz


class TodoList(ListView):
    model = Quiz
    context_object_name = "tasks"