from django.shortcuts import render
# from task.models import Task
from category.models import Category
def home(request):
    data=Category.objects.all()
    return render(request,'home.html',{'data':data})