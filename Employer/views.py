from django.shortcuts import render,redirect
from django.contrib import messages
from Store_manager.models import * 
from django.db.models import Q
from .form import *
from django.contrib.auth import update_session_auth_hash
def employe_view(request):
    users = User.objects.get(id=request.user.id)
    re_employ=employ.objects.get(user=users)
    admin = re_employ
    Request_by=re_employ.Full_Name
    all_emp_request=employe_request_form1_permanent.objects.filter(Request_by=Request_by)   
    context={
        'all_emp_request':all_emp_request,
        'admin':admin,
    } 
    return render(request,'employe/index.html',context)

def emp_request(request):
    user=request.user
    emp=employ.objects.get(user=user)
    Request_by=emp.Full_Name
    Department=(emp.inDepartment)
    request_store=(emp.accessStore)
    checkd_by = employ.objects.get(Q(role = "Dept_Head") & Q(inDepartment=Department))
    if employe_request_form1.objects.filter(Request_by=Request_by).count() !=0:
        employe_request_form1.objects.filter(Request_by=Request_by).delete()
        form1=employe_request_form1.objects.create(request_store=request_store,Request_by=Request_by,Department=Department,checkd_by=checkd_by)
    else:
        form1=employe_request_form1.objects.create(request_store=request_store,Request_by=Request_by,Department=Department,checkd_by=checkd_by)
   
    form1=employe_request_form1.objects.filter(Request_by=Request_by)
    new_form1=form1[0]
    if request.method == "POST":
        employe_request_form2.objects.create(employe_request_form1=new_form1)
    return render(request,'employe/request.html')
def emp_request2(request):
    user=request.user
    emp=employ.objects.get(user=user)
    Request_by=emp.Full_Name
    form1=employe_request_form1.objects.filter(Request_by=Request_by)
    
    newform=form1[0]
    
    emp_req=employe_request_form2.objects.filter(employe_request_form1=newform)
    context={
        'emp_req':emp_req,
    }
    if form1:
        form1=form1[0]
    if request.method == 'POST':
        Description=request.POST.get("desc")
        unit=request.POST.get("unit")
        req_qty=request.POST.get("qty")
        Remark=request.POST.get("remark")
        form2=employe_request_form2.objects.create(employe_request_form1=form1,Description=Description,unit=unit,req_qty=req_qty,Remark=Remark)
    if form2:
        print("created form 2")
    return render(request,'employe/request.html',context)

def complet_request(request):
    user=request.user
    emp=employ.objects.get(user=user)
    Request_by=emp.Full_Name
    form1=employe_request_form1.objects.get(Request_by=Request_by)
    Request_by=form1.Request_by
    Department=form1.Department
    request_store=form1.request_store
    checkd_by=form1.checkd_by
    all_items=employe_request_form2.objects.filter(employe_request_form1=form1)
    for item in all_items:
        Description=item.Description
        unit=item.unit
        req_qty=item.req_qty
        Remark=item.Remark
        employe_request_form1_permanent.objects.create( 
            Request_by=Request_by,
            Department=Department,
            request_store=request_store,
            checkd_by=checkd_by,
            Description=Description,
            unit=unit,
            req_qty=req_qty,
            Remark=Remark,)
    return redirect('employe_dashboard')
    

def reste_request_form(request):
    user=request.user
    emp=employ.objects.get(user=user)
    Request_by=emp.Full_Name
    form1=employe_request_form1.objects.get(Request_by=Request_by)
    employe_request_form2.objects.filter(employe_request_form1=form1).delete()

    return render(request,'employe/request.html',)




# ---------------------- Profile ------------------------

def user_Profile(request):
    users = User.objects.get(id=request.user.id)
    re_employ=employ.objects.get(user=users)
    admin = re_employ
    context= {
        'admin':admin,
    }
    return render(request,'employe/profile/show_profile.html',context)

def edit_Profile(request):
    users = User.objects.get(id=request.user.id)
    re_employ=employ.objects.get(user=users)
    admin = re_employ
    context= {
        'admin':admin,
    }
    
    if request.method == 'POST':
        admin.about = request.POST.get('about')
        admin.phone1 = request.POST.get('phone1')
        admin.phone2 = request.POST.get('phone2')
        admin.address = request.POST.get('address')
        admin.facebook = request.POST.get('facebook')
        admin.telegram = request.POST.get('telegram')
        admin.instagram = request.POST.get('instagram')
        users.first_name = request.POST.get('first_name')
        users.last_name = request.POST.get('last_name')
        users.email = request.POST.get('email')
        admin.save()
        users.save()
        messages.success(request,'Your profile has been updated successfully. ')
        return redirect('emp_user-Profile')
    return render(request,'employe/profile/edit_profile.html',context)

def chage_password(request):
    users = User.objects.get(id=request.user.id)
    re_employ=employ.objects.get(user=users)
    admin = re_employ
    
    form = passwordform(request.user)
    if request.method == 'POST':
        form = passwordform(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('emp_user-Profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = passwordform(request.user)
    context = {
        'form': form,
        'admin':admin,
        }
    return render(request,'employe/profile/chage_pass.html',context)

def emp_chage_profile_pic(request):
    users = User.objects.get(id=request.user.id)
    re_employ=employ.objects.get(user=users)
    admin = re_employ
    context= {
        'admin':admin,
    }
    if len(request.FILES.get('newimg', "")) != 0:
        
        admin.profile_pic.delete()
        admin.profile_pic = request.FILES.get('newimg', "")
        admin.save()
        messages.success(request,'Your profile picture has been updated successfully.')
        return redirect('emp_user-Profile')
    else:
        return render(request,'employe/profile/change_profile_pic.html',context)

def delete_profile_pic(request):
    users = User.objects.get(id=request.user.id)
    re_employ=employ.objects.get(user=users)
    admin = re_employ
    context= {
        'admin':admin,
    }
    if len(admin.profile_pic) != 0:
        admin.profile_pic.delete()
        return redirect('emp_user-Profile')
    return render(request,)
