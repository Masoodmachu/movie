from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from cinimaapp.models import Movie
from cinimaapp.models import CustomUser

from cinimaapp.forms import Movieform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# @login_required()
# def home(request):
#
#     s=Movie.objects.all()
#     return render(request,"home.html",{'m':s})


class HomeView(ListView):
    model=Movie
    template_name="home.html"
    context_object_name='m'


# @login_required()
# def detail(request,n):
#
#     s=Movie.objects.get(id=n)
#     return render(request,"detail.html",{'m':s})

class Detail(DetailView):
    model=Movie
    template_name='detail.html'
    context_object_name='m'

# @login_required()
# def update(request,n):
#     s=Movie.objects.get(id=n)
#
#     if(request.method=='POST'):
#
#         form=Movieform(request.POST,request.FILES,instance=s)
#
#         if form.is_valid():
#             form.save()
#             return home(request)
#
#
#     form=Movieform(instance=s)
#
#     return render(request,"edit.html", {'form':form})

class Update(UpdateView):
    model=Movie
    template_name='edit.html'
    context_name='form'
    fields = ['name', 'year', 'desc', 'image']
    success_url=reverse_lazy('cinimaapp:home')

# @login_required()
# def addmovie(request):
#
#     return render(request,"addmovie")
#
#
#     form=Movieform(instance=s)
#
#     return render(request,"edit.html",{'form':form})


# def delete(request,n):
#     s=Movie.objects.get(id=n)
#     s.delete()
#     return home(request)

class Delete(DeleteView):
    model=Movie
    template_name='delete.html'
    success_url = reverse_lazy('cinimaapp:home')


# @login_required()
# def add(request):
#
#     if(request.method=='POST'):
#
#         name=request.POST['n']
#         desc=request.POST['d']
#         year=request.POST['y']
#
#         image=request.FILES['image']
#
#         s=Movie.objects.create(name=name,desc=desc,year=year,image=image)
#
#         s.save()
#         return home(request)
#
#     return render(request,"addmovie.html")

class AddMovie(CreateView):
    model=Movie
    template_name='addmovie.html'
    fields = ['name','year','desc','image']
    success_url = reverse_lazy('cinimaapp:home')



def register(request):

    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        phonenumber=request.POST['phonenumber']
        address=request.POST['address']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']



        if(cpassword==password):
            user=CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,phonenumber=phonenumber,address=address)
            user.save()
            return login(request)
        else:
            return HttpResponse("Password does not match")

    return render(request,"register.html")

def login(request):

    if(request.method=='POST'):

        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('cinimaapp:home')
        else:
            return HttpResponse("Invalid paasword or user name")

    return render(request,"login.html")

# @login_required
def logout(request):
    auth.logout(request)
    return login(request)


