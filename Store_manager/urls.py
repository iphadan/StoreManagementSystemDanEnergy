from django.urls import path
from .import views
from .views import GeneratePdf


urlpatterns = [
   path('pdf/', GeneratePdf.as_view(),name="pdf"),
   path('',views.store_dashboard,name="store-dashboard"),
   # 
   # -------- profile --------- #
   path('user_Profile',views.user_Profile,name="user-Profile"),
   path('edit_Profile',views.edit_Profile,name="edit-Profile"),
   path('chage_password',views.chage_password,name="chage_password"),
   path('chage_profile_pic',views.chage_profile_pic,name="chage-profile-pic"),
   path('delete_pic',views.delete_profile_pic,name="delete-pic"),
   # -------- End profile --------- #

   path('add_to_store',views.add_to_store,name="add-to-store"),
   path('add_to_store1',views.add_to_store1,name="add-to-store1"),
   path('cheek_request',views.cheeck_request,name="cheeck-request"),
   
   # ---------- Catagory ---------- #
   path('manage_catagory/',views.manage_catagory,name="manage-catagory"),
   path('add_new_catagory',views.add_new_catagory,name="new-catagory"),
   path('catagory_detail/<int:id>',views.catagory_detail,name="catagory-detail"),
   path('catagory_delete/<int:id>',views.delete_catagory,name="catagory-delete"),
   path('item_detail/<int:id>',views.item_detail,name="item_detail"),
   path('item_delete/<int:id>',views.item_delete,name="item-delete"),
   path('add_item/<int:id>',views.add_item,name="add-item"),

   # -------- End Catagory --------- #


   # ---------- Purchase ------------ #
   path('purchase/',views.purchase,name="purchase"),
   path('list_for_purchase/',views.list_for_purchase,name="list_for_purchase"),
   path('check_out/',views.check_out,name="check-out"),
   path('new_action1/',views.new_action1,name="new_action1"),
   path('new_action/',views.new_action,name="new_action"),

   # -------- End Purchase --------- #

   # -------- Chat --------- #
   path('chat/',views.chat,name="chat"),
   path('chat_pepol/<int:id>',views.chat_pepol,name="chat_pepol"),
   path('chat_profile/<int:id>',views.chat_profile,name="chat_profile"),
   
   path('send_message/',views.send_message,name="new"),
   
   # -------- End Chat --------- #

   # -------- Report --------- #
   path('report/',views.report,name="report"),
   # -------- End Report --------- #
]
