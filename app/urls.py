#このファイルは新規作成
from django.urls import path
from . import views
# from .views import TodoList #追加
urlpatterns = [
    path('', views.monndai_show, name='monndai_show'),
    path('templates/seikai', views.move_to_seikaipage, name='move_to_seikaipage'),
    path('templates/fuseikai', views.move_to_fuseikaipage, name='move_to_fuseikaipage'),
    #path('templates/monndai2', views.monndai2_show, name='monndai2_show'),
    path('templates/AddText', views.move_to_AddText, name='move_to_AddText'),
    path("quiz_list",views.TodoList.as_view(), name="list"),
    # path("detail/<int:pk>", views.TodoDetail.as_view(), name="detail"),
    path("create/", views.TodoCreate.as_view(), name="create"),

    # path("", QuizList.as_view(), name="list"),#todoを参考に変更
    # path("detail/<int:pk>", QuizDetail.as_view(), name="detail"),#todoを参考に変更
    # path("create/", QuizCreate.as_view(), name="create"),#todoを参考に変更
]##ここは適宜追加する都度uploadします。 