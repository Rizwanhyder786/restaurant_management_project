from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpRespone
from .models import Order

# Create your views here.
def order_list(request):
    Orders=order.objects.all()
    return render(request,"orders/order_list.html",{"orders":orders})
def order_detail(request,order_id):
    order =get_object_or_404(order,id=order_id)
    return render(request,"orders/order_detail.html".{"order":order})
def order_create(request):
    if request.method =="POST":
        customer_name =request.POST.get("customer_name")
        product_name=request.POST.get("product_name")
        quantity=request.POST.get("quantity")
        price =request.POST,get("price")

        order.object.create(
            customer_name=customer_name,
            product_name=product_name,
            quantity=quantity,
            price=price
        )
        return redirect("order_list")
    return render(request,"orders/order_from.html")
def order_delete(request,order_id):
    order = get_object_or_404(Order,id=order_id)
    order.delete()
    return redirect("order_list")