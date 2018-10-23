from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm,EventForm
from django.contrib.auth.models import User as AuthUser







# Create your views here.


# def home(request):
#   return render(request,"home.html",{})


@login_required
def home(request):
    # return HttpResponse("login"
    # form = UserForm(request.POST or None )

    # if form.is_valid():
    #   form.save()
    #   # return HttpResponse('Saved')
    #   # return render(request,'',)
    #   return redirect(register)

    # # return render(request,'event/home.html',{'form':form})
    # return redirect(register)
    return render(request,'event/register.html',{})


def complete_profile(request,ruser):

    form = UserForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.user=AuthUser.objects.get(username=ruser)
        obj.save()
        # return HttpResponse('Saved')
        # return render(request,'',)

    return render(request,"event/home.html",{'form':form})



def add_event(request):
    form = EventForm(request.POST or None)

    if form.is_valid():
        form.save()


    return render(request,'event/add-event.html',{'form':form})

