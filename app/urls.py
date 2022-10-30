#このファイルは新規作成
from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include
urlpatterns = [
    path('', views.templates, name='templates'),
    path('Q-easy/correct', views.move_to_seikaipage, name='move_to_seikaipage'),
    path('Q-easy/incorrect', views.move_to_fuseikaipage, name='move_to_fuseikaipage'),
    path("Q-easy/quiz_complete/",views.quiz_complete, name="complete"),
    path("Q-easy/create/", views.TodoCreate.as_view(), name="create"),
    path('admin/', admin.site.urls),
    path('login/', views.LoginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),  # Social Django用
]#ここは適宜追加する都度uploadします。