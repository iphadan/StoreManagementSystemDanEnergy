from django.shortcuts import render,redirect
from Store_manager.models import *
from django.db.models import Q
from django.contrib.auth.models import User, Group

from django.contrib import messages
# Create your views here.

def home(request):
    cate = Catagory.objects.all()
    vend = vendor.objects.all()
    dept = department.objects.all()
    cateLength = cate.__len__()
    vendLenth = vend.__len__()
    deptLength = dept.__len__()
    context={
        'cateLength': cateLength,
        'vendLength': vendLenth,
        'deptLength': deptLength
    }
    return render(request,'Company_Admin/Dashboard/index.html',context)

def user_profile(request):
    return render(request,'Company_Admin/EditProfile/show_profile.html')

#----------------- MANAGE EMPLOYEE ---------------#
def manage_employee(request):

    allEmployees = employ.objects.all()
    context = {
        'all_emplyees': allEmployees
    }

    return render(request,'Company_Admin/ManageEmployee/index.html', context)


def add_new_employe(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        userName = request.POST.get('userName')
        password1 = request.POST.get('temporaryPassword')
        password2 = request.POST.get('temporaryPasswordConfirm')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        role = request.POST.get('role')
        Full_Name = firstName +" " + lastName
        if password1 == password2:
            new = User.objects.filter(username=userName)
            if new.count():
                messages.error(request, "User Already Exist")
            else:
                new = User.objects.filter(email=email)
                if new.count():
                    a = new.count()
                   
                    messages.error(request, "Eamil Already Exist")
                else:
                     user = User.objects.create_user(
                         username=userName, email=email, password=password1, first_name=firstName, last_name=lastName)
                     user.save()
                     if user:
                        if role == 'Company_Admin':
                            new_group = Group.objects.get(name='Company_Admin')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender)
                            if newEmployee:
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect("manage-employee")
                        elif (role == 'Dept_Head'):
                            new_group = Group.objects.get(name='Dept_Head')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender)
                            if newEmployee:
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect("manage-employee")
                        elif (role == 'Store_Manager'):
                            new_group = Group.objects.get(name='Store_Manager')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender)
                            if newEmployee:
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect("manage-employee")
                        elif(role == 'Employee'):
                            new_group = Group.objects.get(name='Employe')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender)
                            if newEmployee:
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect("manage-employee")
                        elif(role == 'Finance'):
                            new_group = Group.objects.get(name='Finance')
                            new_group.user_set.add(user)
                            newEmployee = employ.objects.create(user=user,role=role,Full_Name=Full_Name,gender=gender)
                            if newEmployee:
                                messages.success(request,'You Have Successfully Created New Employee')
                                return redirect("manage-employee")
                        
                        
                   

        else:
            messages.error(request, "password not match")

    return render(request,'Company_Admin/ManageEmployee/add_new_employee.html')

#----------------- END of manage Employee ---------------#


#----------------- DEPARTMENTS ---------------#

def departments(request):

    if request.method == 'POST':
        deptId = request.POST.get('deptId')

       

    all_depts = department.objects.all()
    context={
        'all_dept': all_depts
    }
    
    return render(request,'Company_Admin/Departments/index.html', context)

def add_new_department(request):
    DeptHead = employ.objects.filter(role = 'Dept_Head')
    
    context = {
        "departmentHeads" : DeptHead
    }
    if request.method == 'POST':
        departmentName = request.POST.get('departmentName')
        departmentDescription = request.POST.get('departmentDescription')
        
        dept = department.objects.create(departmentName = departmentName,departmentDescription=departmentDescription)
        if dept:
            messages.success(request,'You Have Successfully added new department.')
            
        return redirect('departments')

    return render(request,'Company_Admin/Departments/add_new_department.html', context)

def department_details(request,id):
    DeptHead = employ.objects.filter(role = 'Dept_Head')
    if request.method == 'POST':
        updatedDepartmentName = request.POST.get('updatedDepartmentName')
        departmentId = request.POST.get('departmentId')
        toBeUpdate = department.objects.filter(id=departmentId).update(departmentName=updatedDepartmentName)
        if toBeUpdate:
            messages.success(request,'You Have Successfully updated the department Name')
    selectedDepartment = department.objects.get(pk=id)
    memebers = employ.objects.filter(inDepartment = selectedDepartment.id)
    context={
         "departmentHeads" : DeptHead,
        'selectedDepartment': selectedDepartment,
        'members': memebers
    }
    return render(request,'Company_Admin/Departments/department_details.html', context)
def set_dept_head(request):
    if request.method =="POST":
        dept_id=request.POST.get('departmentId')
        dept_head=request.POST.get('dept_head')
        update_dept=department.objects.get(id=dept_id)
        update_dept.departmentHead = dept_head
        update_dept.save()
        print("dept_id",dept_id)
        print("dept_head",dept_head)
    return redirect('department-details',dept_id)

def department_delete(request,id):
    tobedeleted = department.objects.filter(pk=id).delete()
    if tobedeleted:
        
        messages.success(request,'You Have Successfully deleted the department')
        return redirect('departments')

#----------------- END of Departments ---------------#


#----------------- VENDORS ---------------#
def vendors(request):
    allVendors = vendor.objects.all()
    context = {
        'allVendors': allVendors
    }
    return render(request,'Company_Admin/Vendors/index.html',context)

def vendor_detail(request,id):
    selectedVendor = vendor.objects.get(pk=id)
    context = {
        'selectedVendor': selectedVendor
    }
    return render(request,'Admin/Vendors/vendor_details.html',context)

def add_new_vendor(request):

    if request.method == 'POST':
        # vendorCode = request.POST.get('vendorCode')
        vendorName = request.POST.get('vendorName')
        vendorProducts = request.POST.get('vendorProducts')
        vendorOrigin = request.POST.get('vendorOrigin')
        vendorType = request.POST.get('vendorType')

        ven = vendor.objects.create(vendorName=vendorName,vendorProducts=vendorProducts,vendorOrigin=vendorOrigin,vendorType=vendorType)
        if ven:
            messages.success(request,'You Have Successfully added new vendor.')
            
        return redirect('vendors')

    return render(request, 'Company_Admin/Vendors/add_new_vendor.html')

#----------------- END of VENDORS ---------------#

#----------------- ROLE ---------------#

def role(request):
    
    allRoles = allRole.objects.all()
    context={
        'allRoles': allRoles
    }
    return render(request,'Company_Admin/Role/index.html',context)

def add_new_role(request):
    return render(request, 'Company_Admin/Role/add_new_role.html')

def role_details(request,id):
    selectedRole = allRole.objects.get(pk=id)
    context={
        'selectedRole': selectedRole
    }
    return render(request, 'Company_Admin/Role/role_details.html',context)

#----------------- END of ROLE ---------------#


#----------------- STORE ---------------#
def store(request):
    stores = allStore.objects.all()
    context ={
        'stores': stores
    }
    return render(request,'Company_Admin/Store/index.html', context)

def store_details(request,id):
    all_category = Catagory.objects.filter(store=id)
    all_category.storeId = id
   
    context = {
        'all_category': all_category,
        'storeId':id
    }
   
    return render(request,"Company_Admin/Store/store_detail.html", context)

def add_new_store(request):
    storeKeepers = employ.objects.filter(role = 'Store_Manager')
    context={
        'storeKeepers': storeKeepers
    }

    if request.method == 'POST':
        storeName = request.POST.get('storeName')
        storeDescription = request.POST.get('storeDescription')
        storeKeeper = request.POST.get('storeKeeper')
        storeLocation = request.POST.get('storeLocation')


        addedStore = allStore.objects.create(storeName=storeName,storeDescription=storeDescription,storeKeeper=storeKeeper,storeLocation=storeLocation)
        if addedStore:
            return redirect('store')
        
    return render(request, 'Company_Admin/Store/add_new_store.html', context)

def cat_item_detail(request,id):
    category = Catagory.objects.get(pk=id)
    context={
        'category':category
    }
    return render(request, 'Company_Admin/Store/cat_item_details.html',context)

#----------------- End OF STORE ---------------#

def reports(request):
    return render(request,'Company_Admin/Reports/index.html')

def chat(request):
    chat_group=employ.objects.all()
    if request.method == 'POST':
        user=request.POST.get('serach')
        serch=User.objects.get(username=user)
        chat_group1=employ.objects.get(user=serch)
   
        context={
            
            'chat_group1':chat_group1,
        }
        return render(request,'Company_Admin/chat/index1.html',context)
    context={
      
        'chat_group':chat_group,
    }
    return render(request,'Company_Admin/chat/index.html',context)

def chat_pepol(request,id):
    chat_employ=employ.objects.get(pk=id)
    me=employ.objects.get(pk=request.user.id)
    all_message=chatbot.objects.filter(Q(Q(me_with=chat_employ) | Q(me=chat_employ)) & Q(Q(me_with=me) | Q(me=me)))
    if request.method == 'POST':
        me_with=employ.objects.get(pk=id)
        me=me
        message=request.POST.get('mess')
        newmess=chatbot.objects.create(me_with=me_with,me=me,message=message)
        if newmess:
            return redirect('admin-chat_people',id)
    context={
        'chat_employ':chat_employ,
        'message':all_message,
        'id':id,
        'me':me
    }
    return render(request,'Company_Admin/chat/chat.html',context)
def chat_profile(request,id):
    chat_employ=employ.objects.get(pk=id)
    context={
        'chat_employ':chat_employ,
    }
    return render(request,'Company_Admin/chat/profile.html',context)
def send_message(request):
    me=request.user
    if request.method == 'POST':
       pass
    return redirect('admin-chat_people')