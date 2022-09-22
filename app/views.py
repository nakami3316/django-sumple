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


# #下記はtodoを参考にした
from django.views.generic import ListView, DetailView, CreateView

from django.urls import reverse_lazy

# class QuizDetail(DetailView):
#     model = Quiz
#     context_object_name = "task"

class TodoCreate(CreateView):
    model = Quiz
    fields = "__all__"
    success_url = reverse_lazy("list")

class TodoList(ListView):
    model = Quiz
    context_object_name = "tasks"