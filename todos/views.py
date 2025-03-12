from django.shortcuts import redirect, render

from .forms import TodoForm
from todos.models import Todo

# Create your views here.


def home(request):
    return render(request, "home.html")
    # return HttpResponse("안녕하세요") render 함수는 HttpResponse를 담고있다.


def todo_list(request):
    # select * from todos where complete=0
    todos = Todo.objects.filter(
        complete=False
    )  # objects 객체 변수가 핵심이다. all() 하면 테이블 전체 다 출력
    return render(
        request, "todo/todo_list.html", {"todos": todos}
    )  # todos 값을 딕셔너리 형식으로 같이 넘겨준다.


def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():  # 안의 글자들이 유효한가?
            todo = form.save(commit=False)  # 커밋은 안하고 SQL 쿼리만 실행.
            todo.save()  # 이때 sql 쿼리문이 날아간다
            return redirect("todo_list")
    else:
        form = TodoForm()

    return render(request, "todo/todo_post.html", {"form": form})


# urls.py의 path("<int:pk>", views.todo_detail, name="todo_detail")
def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)  # filter는 1개 이상일때, get은 한개만.
    return render(request, "todo/todo_detail.html", {"todo": todo})


def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect("todo_list")

    else:
        # 레코드를 instance로 지정한다. (한줄 전체 다.)
        form = TodoForm(instance=todo)

    return render(request, "todo/todo_post.html", {"form": form})


def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect("todo_list")


def done_list(request):

    dones = Todo.objects.filter(complete=True)
    return render(request, "todo/done_list.html", {"dones": dones})
