from django.shortcuts import render, redirect
from django.urls import reverse
from account.forms import RegistrationForm, EditProfileForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('account'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'account/register_form.html', args)


def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'account/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('account:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/edit_profile.html', args)