#このファイルは新規作成
from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('', views.templates, name='templates'),
    path('Q-easy/correct', views.move_to_seikaipage, name='move_to_seikaipage'),
    path('Q-easy/incorrect', views.move_to_fuseikaipage, name='move_to_fuseikaipage'),
    path("Q-easy/quiz_complete/",views.quiz_complete, name="complete"),
    path("Q-easy/create/", views.TodoCreate.as_view(), name="create"),
    path('admin/', admin.site.urls),
]#ここは適宜追加する都度uploadします。