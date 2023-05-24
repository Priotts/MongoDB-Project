from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from django.contrib import messages

# Create your views here.

def order_view(request):
    order = Order.objects.all()

    return render(request, 'app/order_view.html', {'order': order})

@login_required
def order(request):
    user = request.user
    if request.method == 'POST':
        try:
            order_type = request.POST.get('order_type')
            price = float(request.POST.get('price'))
            quantity = float(request.POST.get('quantity'))
            total_cost = price * quantity
        except ValueError:
            messages.error(request, 'Invalid input')
            return redirect('order')
        # Sell
        if order_type == 'Sell':
            if user.userprofile.walletbtc >= quantity:
                order = Order.objects.create(profile=user.userprofile, price=price, quantity=quantity, order_type=order_type, order_status='open')
                execute_sell_order(order)
                messages.success(request, 'Order created')
                return redirect('order')
            else:
                messages.error(request, 'Not enough BTC')
                return redirect('order')
        # Buy 
        if order_type == 'Buy':
            if user.userprofile.usd >= total_cost:
                order = Order.objects.create(profile=user.userprofile, price=price, quantity=quantity, order_type=order_type, order_status='open')
                execute_buy_order(order)
                messages.success(request, 'Order created')
                return redirect('order')
            else:
                messages.error(request, 'Not enough USD')
                return redirect('order')
    c_messages = messages.get_messages(request)
    return render(request, 'app/order.html', {'user': user, 'c_messages': c_messages})

def execute_buy_order(order):
    if order.order_type == 'Buy':
        sell_orders = Order.objects.filter(order_type='Sell', order_status='open', price__lte=order.price).exclude(profile=order.profile).order_by('price')
        for sell_order in sell_orders:
            if sell_order.quantity <= order.quantity:
                # Update the wallets of the users involved in the transaction
                sell_order.profile.walletbtc -= sell_order.quantity
                sell_order.profile.usd += order.price * sell_order.quantity
                order.profile.walletbtc += sell_order.quantity
                order.profile.usd -= order.price * sell_order.quantity
                # Update the profit of the profiles
                order.profile.profit -= order.price * sell_order.quantity
                sell_order.profile.profit += order.price * sell_order.quantity
                #update the quantity of the order 
                order.quantity -= sell_order.quantity
                sell_order.quantity = 0
                sell_order.order_status = 'closed'
                #save the changes
                sell_order.profile.save()
                sell_order.save()
                if order.quantity == 0:
                    order.order_status = 'closed'

                    break
            #sell_order.quantity > order.quantity
            else:
                # Update the wallets of the users involved in the transaction
                sell_order.profile.walletbtc -= order.quantity 
                sell_order.profile.usd += order.price * order.quantity
                order.profile.walletbtc += order.quantity 
                order.profile.usd -= order.price * order.quantity
                # Update the profit of the profiles
                order.profile.profit -= order.price * order.quantity
                sell_order.profile.profit += order.price * order.quantity
                #update the quantity of the order
                sell_order.quantity -= order.quantity
                order.quantity = 0 
                #save the changes
                sell_order.save()
                sell_order.profile.save()
                order.order_status = 'closed'
                break
        #save the changes
        order.profile.save()
        order.save()

def execute_sell_order(order):
    if order.order_type == 'Sell':
        buy_orders = Order.objects.filter(order_type='Buy', order_status='open', price=order.price).exclude(profile=order.profile).order_by('-price')
        for buy_order in buy_orders:
            if buy_order.quantity <= order.quantity:
                # Update the wallets of the users involved in the transaction
                buy_order.profile.walletbtc += buy_order.quantity
                buy_order.profile.usd -= order.price * buy_order.quantity
                order.profile.walletbtc -= buy_order.quantity
                order.profile.usd += order.price * buy_order.quantity
                # Update the profit of the profiles
                order.profile.profit += order.price * buy_order.quantity
                buy_order.profile.profit -= order.price * buy_order.quantity
                #update the quantity of the order
                order.quantity -= buy_order.quantity
                buy_order.quantity = 0
                buy_order.order_status= 'closed'
                buy_order.save()
                buy_order.profile.save()

                if order.quantity == 0:
                    order.order_status = 'closed'
                    break
            #buy_order.quantity > order.quantity
            else:
                buy_order.profile.walletbtc += order.quantity
                buy_order.profile.usd -= order.price * order.quantity
                order.profile.walletbtc -= order.quantity
                order.profile.usd += order.price * order.quantity
                # Update the profit of the profiles
                order.profile.profit += order.price * order.quantity
                buy_order.profile.profit -= order.price * order.quantity
                #update the quantity of the order
                buy_order.quantity -= order.quantity
                order.quantity = 0
                buy_order.save()
                buy_order.profile.save()
                order.order_status = 'closed'
                break
        order.profile.save()
        order.save()