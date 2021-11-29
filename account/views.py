from .forms import CreateUserForm, UpdateProfile, UpdateUser
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from doctor.models import Booking
from django.views.generic.edit import UpdateView

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect!')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def RegistrationPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account Was Created for ' + username)
            return redirect('/login')

    context = {
        'forms': form
    }
    return render(request, 'registration.html', context)


@login_required(login_url='login')
def ProfileView(request):
    form = UpdateUser()
    profile = UpdateProfile()

    if request.method == 'POST':
        form = UpdateUser(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')

    booking = Booking.objects.filter(
        booker=request.user.id).order_by('complete')
    context = {
        'forms': form,
        'profiles': profile,
        'booking': booking
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def ProfileUpdate(request):
    profile = UpdateProfile()

    if request.method == 'POST':
        profile = UpdateProfile(
            request.POST, request.FILES, instance=request.user.profile)
        if profile.is_valid():
            profile.save()
            return redirect('/profile')
    context = {
        'profiles': profile
    }
    return render(request, 'profile-form.html', context)

