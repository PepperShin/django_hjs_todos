from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "home.html")
    # return HttpResponse("안녕하세요") render 함수는 HttpResponse를 담고있다.
