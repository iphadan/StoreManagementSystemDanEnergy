from django.urls import path
from .import views
urlpatterns = [
   path('',views.login_view,name="login"),
   path('log_out',views.logout_view,name="log-out"),
   
]
