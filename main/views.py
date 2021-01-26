from django.shortcuts import render, HttpResponse,redirect
from .models import Todo
from .models import Book

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
    books=Book.objects.all()
    return render(request, "books.html", {"books":books})

def add_book(request):
    form = request.POST 
    books = Book(
        title=form["title"],
        subtitle=form["subtitle"],
        description=form["description"],
        price=form["price"],
        genre=form["genre"],
        author=form["author"],
        year=form["date"][:10]
    )
    books.save()

    return redirect(Book)

def delete_todo(request,id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect(test)
    
def mark_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_favorite=True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_favorite=False
    todo.save()
    return redirect(test)

def close_todo(request,id):
    todo = Todo.object.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)