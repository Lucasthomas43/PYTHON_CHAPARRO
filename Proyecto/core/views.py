from django.shortcuts import redirect, render

from . import forms, models

###DEFINIENDO VIEWS PARA LOS MODELOS ####
def index(request):
    return render(request, "core/index.html")


def product_list(request):
    consulta = models.Producto.objects.all()
    contexto = {"products": consulta}
    return render(request, "core/products_list.html", contexto)

def product_create(request):
    if request.method == "POST":
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products_list")
        
        
    else:
        form = forms.ProductForm()
        return render(request, "core/product_create.html", {"form": form})

def login(request):
    consulta = models.Producto.objects.all()
    contexto = {"products": consulta}
    return render(request, "core/login.html", contexto)

def register(request):
    consulta = models.Producto.objects.all()
    contexto = {"products": consulta}
    return render(request, "core/register.html", contexto)



