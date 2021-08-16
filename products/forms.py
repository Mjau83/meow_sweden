from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'sku', 'name', 'description',
                  'price', 'image_url', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
<<<<<<< HEAD
            field.widget.attrs['class'] = 'border-black rounded-0'
=======
            field.widget.attrs['class'] = 'border-black rounded-0'
>>>>>>> 105c4712cab185b954129b1e7e159af6382a4296
