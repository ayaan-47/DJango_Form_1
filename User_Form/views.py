from django.shortcuts import render, redirect
from .models import User_Forms
from .forms import UsrForm
# Create your views here.


def index(request):
    us=User_Forms.objects.order_by('title')
    context = {'us':us}
    return render(request,'index.html',context)

def usform(request):
    if request.method=='POST':
        form = UsrForm(request.POST)
        if form.is_valid():
            new_req = User_Forms(title=request.POST['ustitle'],description=request.POST['usdescription'])
            new_req.save()
            return redirect('index')
    else:
        form=UsrForm()
    context={'form':form}




    return render(request,'usform.html',context)