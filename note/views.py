from django.shortcuts import render,redirect
from . models import *

# Create your views here.
def InsertPageView(request):
    return render(request,"app/insert.html")



def InsertData(request):
    title=request.POST['Ttitle']
    desc=request.POST['Tdesc']
    #insert data into table
    newuser = TaskTable.objects.create(TaskTitle=title,TaskDescriptions=desc)
    #after insert data redirect to showpage 
    return redirect('showpage')


def ShowPage(request):
    #for fetching all the data from table
    all_data = TaskTable.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

# now for edit page
def EditPage(request,pk):
    get_data = TaskTable.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

def UpdateData(request,pk):
    udata = TaskTable.objects.get(id=pk)
    udata.TaskTitle = request.POST['Ttitle']
    udata.TaskDescriptions = request.POST['Tdesc']
    # query for update
    udata.save()
    #after update redirect to showpage
    return redirect('showpage')

def DeleteData(request,pk):
    Ddata = TaskTable.objects.get(id=pk)
    # quiry for Delete data

    Ddata.delete()
    return redirect('showpage')