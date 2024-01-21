from django import forms
from .models import Producto  # Asegúrate de importar tu modelo

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto  # Especifica el modelo asociado
        fields = "__all__"
