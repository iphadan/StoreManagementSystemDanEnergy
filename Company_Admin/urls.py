from django.urls import path
from .import views

urlpatterns = [
    path('admin-dashboard', views.home, name='admin-dashboard'),
    path('users-profile',views.user_profile,name='users-profile'),

    # MANAGE EMPLOYEE
    path('manage-employee', views.manage_employee, name='manage-employee'),
    path('add-new-employe',views.add_new_employe, name='add-new-employe'),

    # DEPARTMENT
    path('departments', views.departments, name='departments'),
    path('add-new-department',views.add_new_department,name='add-new-department'),
    path('department-details/<int:id>',views.department_details,name='department-details'),
    path('set_dept_head',views.set_dept_head,name='set_dept_head'),
    

    # Vendors
    path('vendors', views.vendors, name='vendors'),
    path('add-new-vendor',views.add_new_vendor,name='add-new-vendor'),
    path('vendor-detail/<int:id>', views.vendor_detail, name='vendor-detail'),

    
    # Role
    path('role', views.role, name='role'),
    path('add-new-role',views.add_new_role,name='add-new-role'),
    path('role-details/<int:id>',views.role_details,name='role-details'),

    # Store
    path('store', views.store, name='store'),
    path('store-details/<int:id>', views.store_details, name='store-details'),
    path('add-new-store',views.add_new_store,name='add-new-store'),
    path('cat-item-detail/<int:id>',views.cat_item_detail,name='cat-item-detail'),
    path('department-delete/<int:id>',views.department_delete,name='department-delete'),

    # 
    path('reports', views.reports, name='reports'),
    
  

     # -------- Chat --------- #
   path('chat/',views.chat,name="admin-chat"),
   path('chat_pepol/<int:id>',views.chat_pepol,name="admin-chat_people"),

   path('chat_profile/<int:id>',views.chat_profile,name="admin-chat_profile"),
   path('send_message/',views.send_message,name="new"),
   
   # -------- End Chat --------- #

]