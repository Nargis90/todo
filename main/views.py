from django.shortcuts import render, HttpResponse,redirect
from .models import Todo
from .models import Books

# Create your views here.
def homepage(request):
    return render(request,"index.html")

def test(request):
    todo_list = Todo.objects.all()
    return render(request,"test.html", {"todo_list":todo_list})   

def second(request):
    return HttpResponse("test 2 page")


def third(request):
    return HttpResponse("This is page test3")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    print(text)
    todo = Todo(text=text)
    todo.save()
    return redirect(test)

def books(request):
    books=Books.objects.all()
    return render(request, "books.html", {"books":books})

