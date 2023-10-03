from django.shortcuts import render,redirect
from django.contrib import messages
from Store_manager.models import *
from django.db.models import Q
from django.db.models import Q
def dept_head(request):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    dept_head=exploreU.Full_Name
    dept_name=department.objects.get(departmentHead=dept_head)
    indep=dept_name.departmentName
    exploreU.inDepartment=dept_name.departmentName
    exploreU.save()
    all_emp=employ.objects.filter(inDepartment=indep)
    all_request=employe_request_form1_permanent.objects.filter(Q(checkd_by=exploreU) & Q(dept_head_Action="Pending"))
    No_pending_req=all_request.count()
    context = {
        'userData' : exploreU,
        'dept_name':dept_name,
        'all_emp':all_emp,
        'No_pending_req':No_pending_req,
    }
    return render(request,'Department_head/index.html', context)

def add_employe(request):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    dept_head=exploreU.Full_Name
    dept_name=department.objects.get(departmentHead=dept_head)
    allEmps = employ.objects.filter(Q(role = "Employee") & Q(inDepartment = None))
   
    context = {
        'allEmps' : allEmps
    }
    if request.method == 'POST':
        newemp=request.POST.get('emp')
        check=request.POST.get('check')
        newadd_emp=employ.objects.get(id=newemp)
        print("--------------------")
        print(newadd_emp)
        print("--------------------")
        newadd_emp.inDepartment=dept_name.departmentName
        if check:
            newadd_emp.Thechnologist=True
        newadd_emp.save()
        return redirect('dept-dashboard')
    return render(request,'Department_head/add_employe.html',context)
def add_emp(request):

    if request.method == 'POST':
        newempl=request.POST.get('emp')
        print("----------------")
        print(newempl)
        return redirect('dept-dashboard')


def cheek_request(request):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    all_request=employe_request_form1_permanent.objects.filter(checkd_by=exploreU)
    context={
        'all_request':all_request,
    }
    return render(request,'Department_head/check_request.html',context)
def dept_approved(request,id):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    emp_request=employe_request_form1_permanent.objects.get (Q(checkd_by=exploreU) & Q(pk=id))
    emp_request.dept_head_Action="Approved"
    emp_request.save()
    return redirect('check_request')

def dept_reject(request,id):
    curretnUser = request.user
    exploreU = employ.objects.get(user = curretnUser)
    emp_request=employe_request_form1_permanent.objects.get (Q(checkd_by=exploreU) & Q(pk=id))
    emp_request.dept_head_Action="Rejected"
    emp_request.save()
    return redirect('check_request')
def make_request(request):
    return render(request,'Department_head/make_request.html',)