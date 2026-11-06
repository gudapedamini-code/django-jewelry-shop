from .models import Category, Cart
from django.db import OperationalError, ProgrammingError


def store_menu(request):
    try:
        categories = list(Category.objects.filter(is_active=True))
    except Exception:
        # Table may not exist yet or DB not ready
        categories = []
    context = {
        'categories_menu': categories,
    }
    return context


def cart_menu(request):
    if request.user.is_authenticated:
        try:
            cart_items = list(Cart.objects.filter(user=request.user))
        except Exception:
            cart_items = []
        context = {
            'cart_items': cart_items,
        }
    else:
        context = {}
    return context