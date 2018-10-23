from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm,EventForm
from django.contrib.auth.models import User as AuthUser
from .models import User,Event







# Create your views here.


# def home(request):
#   return render(request,"home.html",{})


@login_required
def home(request):
    try:
        user=User.objects.get(user=request.user)
    except:
        # user = 
        # pass
        # user = AuthUser.objects.get(username=request.user)
        # print(type(user))
        # user=request.user
        pass
    # return HttpResponse("login"
    # form = UserForm(request.POST or None )

    # if form.is_valid():
    #   form.save()
    #   # return HttpResponse('Saved')
    #   # return render(request,'',)
    #   return redirect(register)

    # # return render(request,'event/home.html',{'form':form})
    # return redirect(register)
    return render(request,'event/register.html',{'ruser':user})


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



def get_event(request):
    obj = Event.objects.all()

    print("%^%^&%^%^%^^")
    print(obj)

    return render(request,"event/event-list.html",{'event':obj})


def profile(request):
    obj = User.objects.get(user=request.user)
    print(obj)
    return render(request,'event/profile.html',{'obj':obj})