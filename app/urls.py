#このファイルは新規作成
from django.urls import path
from . import views
urlpatterns = [
    path('', views.templates, name='templates'),
    path('Q-easy/correct', views.move_to_seikaipage, name='move_to_seikaipage'),
    path('Q-easy/incorrect', views.move_to_fuseikaipage, name='move_to_fuseikaipage'),
    path("quiz_list",views.TodoList.as_view(), name="list"),
    path("quiz_complete",views.TodoList.as_view(), name="complete"),
    # path("detail/<int:pk>", views.TodoDetail.as_view(), name="detail"),
    path("create/", views.TodoCreate.as_view(), name="create"),
]##ここは適宜追加する都度uploadします。 