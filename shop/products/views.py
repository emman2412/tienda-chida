from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Category, Product, Trademark
from .forms import ProductForm
from cart.forms import CartAddProductForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.db.models import Q

# Create your views here.

class StaffRquiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRquiredMixin, self).dispatch(request, *args, **kwargs)

def product_list(request):
    products = Product.objects.filter(available=True)
    category = None
    categories = Category.objects.all()
    trademark = None
    trademarks = Trademark.objects.all()
    context = {
        'category': category,
        'categories': categories,
        'trademark': trademark,
        'trademarks': trademarks,
        'products': products,
    }
    return render(request, 'products/list.html', context)
    
def category(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'products/list.html', context)

def trademark(request, trademark_slug=None):
    trademark = None
    trademarks = Trademark.objects.all()
    products = Product.objects.filter(available=True)
    if trademark_slug:
        trademark = get_object_or_404(Trademark, slug=trademark_slug)
        products = Product.objects.filter(trademark=trademark)
    context = {
        'trademark': trademark,
        'trademarks': trademarks,
        'products': products
    }
    return render(request, 'products/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'products/detail.html', context)

@method_decorator(staff_member_required, name='dispatch')
class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

@method_decorator(staff_member_required, name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('products:update', args=[self.object.id, self.object.slug]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')


def search(request):
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        results = Product.objects.filter(available=True)
    context = {
        'products': results,
    }
    return render(request, 'products/list.html', context)
    
def order_name(request):
    results = Product.objects.order_by('name')
    context = {
        'products': results,
    }
    return render(request, 'products/list.html', context)

def order_price(request):
    results = Product.objects.order_by('price')
    context = {
        'products': results,
    }
    return render(request, 'products/list.html', context)