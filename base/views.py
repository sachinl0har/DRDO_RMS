import re
from django.shortcuts import render, redirect
from .models import BookUser, Room, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm, BookUserForm, UserForm


# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User Doesn\'t Exist')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')

    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
    context = {'form':form}
    return render(request, 'base/login_register.html', context)

def index(request):
    return render(request, 'base/home.html')

@login_required(login_url='login')
def dashboard(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/rooms.html', context)

@login_required(login_url='login')
def room(request, pk):
    room = Room.objects.get(id = pk)
    events = BookUser.objects.filter(bookFor = room)
    form = BookUserForm()
    if request.method == 'POST':
        BookUser.objects.create(
            name = request.user,
            title = request.POST.get('title'),
            bookFor = room,
            bookStartTime = request.POST.get('bookStartTime'),
            bookEndTime = request.POST.get('bookEndTime'),
            isBooked = False,
        )
        return redirect('rooms')
    context = {'room':room, 'form':form, 'events':events}
    return render(request, 'base/room.html', context)

@login_required(login_url='login')
def bookings(request, pk):
    room = Room.objects.get(id = pk)
    events = BookUser.objects.filter(bookFor = room)
    context = {'events':events}
    return render(request, 'base/bookings.html', context)

def userProfile(request):
    user = User.objects.get(id=request.user.id)
    context = {'user':user}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    context = {'form':form}
    return render(request, 'base/update-user.html', context)