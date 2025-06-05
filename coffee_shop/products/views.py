from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from .models import Product
from django.contrib import messages
from django.shortcuts import render, redirect



# Create your views here.
class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_products')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'files': self.request.FILES})  # <-- ESTA LÍNEA
        return kwargs


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list_product.html'
    context_object_name = 'products'

    
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Se agregó el producto exitosamente!')
            # Puedes redirigir a la misma vista para evitar doble POST
            return redirect('add_products')  
    else:
        form = ProductForm()
    return render(request, 'products/add_products.html', {'form': form})