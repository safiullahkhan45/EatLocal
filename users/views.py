from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ProfileUpdateForm
from cart.models import Cart
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('cart')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):

    try:
        items = Cart.objects.get(profile=request.user.profile)
    except Cart.DoesNotExist:
        items = Cart(
                    profile = request.user.profile,
                    ref_name = request.user.username
                )
        items.save()

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    else:
        form = ProfileUpdateForm(
                initial= {
                    'plan': request.user.plan
                }
            )

    context = {
        'form': form,
        'items': items
    }

    return render(request, 'users/profile.html', context)

