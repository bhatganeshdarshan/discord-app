from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Room,Topic
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# rooms=[
#     {'id':1,'name':'lets learn python '},
#     {'id':2,'name':'design with me'},
#     {'id':3,'name':'front end developers '},

# ]

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User Doesnot exist')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password doesnot match')

    context = {}
    return render(request,'main/login_register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')


def home(request):
    q =  request.GET.get('q') if request.GET.get('q') != None else ''
    rooms=Room.objects.filter(Q(topic__name__icontains = q) | Q(name__icontains = q) | Q(description__icontains = q))
    topic=Topic.objects.all() 
    room_count=rooms.count()
    context={'rooms':rooms,'topic':topic,'room_count':room_count}
    return render(request,'main/home.html',context)
def room(request,pk):
    room = Room.objects.get(id = pk)
    context = {'room':room}
    return render(request,'main/room.html',context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'main/room_form.html',context)

@login_required(login_url='/login')
def updateRoom(request,pk):
    room= Room.objects.get(id=pk)
    form= RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed here !! ")

    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'main/room_form.html',context)

@login_required(login_url='/login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'main/delete.html',{'obj':room})

