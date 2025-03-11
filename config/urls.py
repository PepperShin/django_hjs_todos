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
from django.urls import include, path

from config import settings

# http://127.0.0.1:8000/admin
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todos.urls")),  # root로 오면 todos.urls 파일을 참조하라
]

# dev_3
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
