from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from django.contrib import messages
from shop.recommender import Recommender


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product, quantity=cd["quantity"], override_quantity=cd["override"]
        )
        messages.success(request, f'{product.translations.name} added to cart!')

    return redirect(product.get_absolute_url())


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        print(item)
        item["update_quantity_form"] = CartAddProductForm(
            initial={"quantity": item["quantity"], "override": True}
        )
    coupon_apply_form = CouponApplyForm()
    context = {"cart": cart, "coupon_apply_form": coupon_apply_form}
    r = Recommender()
    cart_products = [item['product'] for item in cart]
    if len(cart_products) >= 1:
        recommended_products = r.suggest_products_for(
            cart_products, max_results=4)
        context["recommended_products"] = recommended_products
    return render(request, "cart/cart-detail.html", context)


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")
