from django.shortcuts import render, redirect
from crudapp.forms import StudentsForm
from crudapp.models import Students
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass

    else:
        form = StudentsForm()
        return render(request, 'index.html',{'form':form})

@csrf_protect
def view(request):
    students = Students.objects.all()
    return render(request, "views.html", {"students":students})

@csrf_protect
def edit(request, id):
    student = Students.objects.get(id=id)
    return render(request, 'edit.html',{'student':student})

@csrf_protect
def delete(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    return redirect('/view')

@csrf_protect
def update(request,id):
    student = Students.objects.get(id=id)

    if request.method == "POST":
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass

    else:
        form = StudentsForm(instance=student)
        return render(request, 'index.html', {'form': form})