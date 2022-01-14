from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfielUpdateForm
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #this tells us whether our form is valid or not
            form.save() #form.save() method -> saves the user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account was successfully created! You can now log in')
            return redirect('login') 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfielUpdateForm(request.POST, request.FILES,  instance = request.user.profile )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile was successfully updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfielUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
