from django.shortcuts import render ,redirect
from .models import Room,Topic
from .forms import RoomForm
# rooms=[
#     {'id':1,'name':'lets learn python '},
#     {'id':2,'name':'design with me'},
#     {'id':3,'name':'front end developers '},

# ]

def home(request):
    q =  request.GET.get('q') if request.GET.get('q') != None else ''
    rooms=Room.objects.filter(topic__name__icontains = q)
    topic=Topic.objects.all() 
    context={'rooms':rooms,'topic':topic}
    return render(request,'main/home.html',context)
def room(request,pk):
    room = Room.objects.get(id = pk)
    context = {'room':room}
    return render(request,'main/room.html',context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'main/room_form.html',context)


def updateRoom(request,pk):
    room= Room.objects.get(id=pk)
    form= RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'main/room_form.html',context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'main/delete.html',{'obj':room})

