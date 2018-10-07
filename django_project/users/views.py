from django.shortcuts import render, redirect
from django.http.response import Http404
from django.contrib import messages
# custom user form imported
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# preventor for witout account visiting profile page.
from django.contrib.auth.decorators import login_required


def register(request):
    # form validation check.
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # saves user to database
            username = form.cleaned_data.get('username')
            # sending modified success alert messages to templates.
            messages.success(
                request, f'Your account has been created! You are able to log in {username} !')
            return redirect('login')  # redirection to home page.

    else:  # if there is no form for validation.
        form = UserRegisterForm()
    context = {
        'form': form  # pasing form to html templates
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Your account has been updated succesfully.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
