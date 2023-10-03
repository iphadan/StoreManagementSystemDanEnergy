from django.shortcuts import render
from django.contrib import messages
def finance_view(request):
    
    return render(request,'Finance/index.html',)