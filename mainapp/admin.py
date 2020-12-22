from django import forms
from django.contrib import admin
from django.forms import CheckboxSelectMultiple




from mptt.admin import MPTTModelAdmin
from mptt.models import TreeManyToManyField
from django.forms import ModelChoiceField,ModelForm, ValidationError
from .models import *
from django.utils.safestring import mark_safe


class MyImageAdminForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


class ProductAdminForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)



class filterCategory(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(filterCategory, self).__init__(*args,**kwargs)
        self.fields['category'].queryset = Category.objects.filter(children=None)


class ProductAdmin(admin.ModelAdmin):
    form = filterCategory
    formfield_overrides = { TreeManyToManyField:{'widget':CheckboxSelectMultiple},}

class Qwerty(admin.ModelAdmin):
    model=ProductFeatures


admin.site.register(Category,Qwerty)
admin.site.register(ProductFeatures)

admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)

admin.site.register(Product,ProductAdmin)
admin.site.register(MyImage)
admin.site.register(Rewiews)
admin.site.register(ProductFeatureValidators)


admin.site.site_title="Администрация магазина"
admin.site.site_header="Магазин"
