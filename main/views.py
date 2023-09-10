from django.shortcuts import render ,redirect
from .models import Room
from .forms import RoomForm
# rooms=[
#     {'id':1,'name':'lets learn python '},
#     {'id':2,'name':'design with me'},
#     {'id':3,'name':'front end developers '},

# ]

def home(request):
    rooms=Room.objects.all() 
    context={'rooms':rooms}
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

