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
    list_display= ( 'id','title', 'category', 'price', 'available')
    list_display_links=('id','title')
    list_editable=('available',)
    search_fields= ('title','descripton','price')
    form = filterCategory
    formfield_overrides = { TreeManyToManyField:{'widget':CheckboxSelectMultiple},}


# class MyTopImageInline(admin.TabularInline):
#     verbose_name='Топ изображения'
#     model=MyTopImage


# class MyTopimageAdmin(admin.ModelAdmin):
#     inlines = [
#         MyTopImageInline,
#         ]


class Qwerty(admin.TabularInline):
    model=ProductFeatures


class ProductFeaturesInline(admin.TabularInline):
    model = ProductFeatureValidators


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductFeaturesInline]


# class  MyTopImageInline(admin.TabularInline):
#     model = MyTopImage

# class MyTopImageAdmin(admin.ModelAdmin):
#     inlines = [MyTopImage]


admin.site.register(Category,CategoryAdmin)
admin.site.register(TopText)


admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)

admin.site.register( MyTopImage)


admin.site.register(Product,ProductAdmin)
admin.site.register(MyImage)
admin.site.register(Rewiews)
admin.site.register(ProductFeatureValidators)


admin.site.site_title="Администрация магазина"
admin.site.site_header="Магазин"
