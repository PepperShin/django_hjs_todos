"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    이 내용들을 대부분 개발자들이 지운다.(나중에 참고 후 제거 결정.)
"""

from django.contrib import admin
from django.urls import path

from todos import views  # views 모듈 임포트

# http://127.0.0.1:8000/admin
urlpatterns = [
    path(
        "", views.todo_list, name="todo_list"
    ),  # views.py 파일의 home 함수를 callback 함수로 받는다.
    path("post/", views.todo_post, name="todo_post"),
    # http://127.0.0.1:8000/todo?number=1&name=ghlqkf 스트링 쿼리
    # http://127.0.0.1:8000/todo/{1}/ + get, post, put, delete. 변수화
    path("<int:pk>", views.todo_detail, name="todo_detail"),  # dev_4
]
