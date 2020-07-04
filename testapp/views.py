from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def list_All_data(request):
    emp=Employee.objects.all()
    return render(request,'testapp/index.html',{'emp':emp})
def insert_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/display/')
    return render(request,'testapp/insert.html',{'form': form})
def update_view(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return redirect('/display/')
    return render(request, 'testapp/update.html', {'emp': emp})
def delete_view(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/display/')