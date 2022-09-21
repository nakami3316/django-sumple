#このファイルは新規作成
from django.urls import path
from . import views

urlpatterns = [
    path('', views.monndai_show, name='monndai_show'),
    path('templates/seikai', views.move_to_seikaipage, name='move_to_seikaipage'),
    path('templates/fuseikai', views.move_to_fuseikaipage, name='move_to_fuseikaipage'),
    path('templates/monndai2', views.monndai2_show, name='monndai2_show'),
]##ここは適宜追加する都度uploadします。 