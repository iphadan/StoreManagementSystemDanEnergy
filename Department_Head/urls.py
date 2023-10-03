from django.urls import path
from .import views
urlpatterns = [
   path('',views.dept_head,name="dept-dashboard"),
   path('add_employe',views.add_employe,name="add_employe"),
   path('check_request',views.cheek_request,name="check_request"),
   path('make_request',views.make_request,name="make_request"),
   path('add_emp',views.add_emp,name="add_emp"),
   path('dept_approved/<int:id>',views.dept_approved,name="aprove_request"),
   path('dept_reject/<int:id>',views.dept_reject,name="reject_request"),
   

   
   
    
]