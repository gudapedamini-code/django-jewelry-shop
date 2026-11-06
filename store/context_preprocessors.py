from .models import Category, Cart
from django.db import OperationalError, ProgrammingError


def store_menu(request):
    try:
        categories = Category.objects.filter(is_active=True)
    except (OperationalError, ProgrammingError):
        # Table may not exist yet (migrations not applied)
        categories = []
    context = {
        'categories_menu': categories,
    }
    return context


def cart_menu(request):
    if request.user.is_authenticated:
        try:
            cart_items = Cart.objects.filter(user=request.user)
        except (OperationalError, ProgrammingError):
            cart_items = []
        context = {
            'cart_items': cart_items,
        }
    else:
        context = {}
    return context