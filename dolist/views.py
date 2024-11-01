from django.shortcuts import render
from . models import ToDolist
# Create your views here.
def index(request):
    todo_items = ToDolist.objects.order_by('id')
    context = {'todo_items' : todo_items}
    return render(request, 'dolist/index.html')