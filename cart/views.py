from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from menu.models import Menu
from users.models import Account
from .forms import CartItemForm
from datetime import datetime
# Create your views here.

def cart_item_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = CartItemForm()
        else:
            cartitem = CartItem.objects.get(pk=id)
            form = CartItemForm(instance = cartitem)
        return render(request, 'cart/schedule.html', {'form': form})

    else:
        if id == 0:
            form = CartItemForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            cartitem = CartItem.objects.get(pk=id)
            form = CartItemForm(request.POST, instance = cartitem)
            if form.is_valid():
                form.save()
            else:
                print('Invalid form')

        return redirect('cart')


def addtocart(request, id):
    person = Account.objects.get(username=request.user.username)
    cart = Cart.objects.get(profile=request.user.profile)
    max_total = person.plan.max_meals
    total_added = cart.total
    print(str(cart.total) + 'Outside')

    if total_added < max_total:
        meal = Menu.objects.get(pk=id)
        cart_item = CartItem(item=meal, time_desired=datetime.now())
        cart_item.save()

        cart.meals.add(cart_item)
        cart.total += 1
        cart.save()
        print(str(cart.total) + 'Inside')

    else:
        print('Unable to add')


    return HttpResponseRedirect(reverse('cart'))

@login_required
def cart(request):

    menus = Menu.objects.all()
    try:
        items = Cart.objects.get(profile=request.user.profile)
    except Cart.DoesNotExist:
        items = Cart(
                    profile = request.user.profile,
                    ref_name = request.user.username
                )
        items.save()

    context = {
        'menus': menus,
        'items': items
    }

    return render(request, 'cart/selectmeals.html', context)

@login_required
def delete_cart_item(request, id):
    cart = Cart.objects.get(profile=request.user.profile)
    item = CartItem.objects.get(pk=id)
    item.delete()
    cart.total -= 1
    cart.save()

    return redirect('cart')

# @login_required
# def paid(request):
#     cart = Cart.objects.get(profile=request.user.profile)
#     cart.paid = True
#     cart.save()

#     return redirect('profile')

@login_required
def checkout_form(request):

    return render(request, 'cart/checkout.html')
