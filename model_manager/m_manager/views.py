from django.shortcuts import render
from .models import A
# Create your views here.
def home(request):
    data = A.abc.all()
    return render(request,'home.html',{'data':data})
