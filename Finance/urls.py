from django.urls import path
from .import views
urlpatterns = [
   path('',views.finance_view,name="finance_dashboard"),
]