from django import forms
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from mptt.admin import MPTTModelAdmin
from mptt.models import TreeManyToManyField
from django.forms import ModelChoiceField,ModelForm, ValidationError
from .models import *
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
# from ckeditor_uploader.widgets import 


class ContactAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Rewiews
        fields = '__all__'


class ContactsAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    list_display= ( 'id','title',)
    list_display_links=('id','title')


class ReturnsAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Rewiews
        fields = '__all__'


class ReturnsAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    list_display= ( 'id','title',)
    list_display_links=('id','title')





class AboutAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = AboutUs
        fields = '__all__'


class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm
    list_display= ( 'id','title',)
    list_display_links=('id','title')



class DeliveryAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryAdminForm
    list_display= ( 'id','title',)
    list_display_links=('id','title')



class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = '__all__'


# class ReviewsAdminForm(forms.ModelForm):
#     text = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Rewiews
#         fields = '__all__'


class RewiewsAdmin(admin.ModelAdmin):
    # form = ReviewsAdminForm
    list_display= ( 'id','name','product')
    list_display_links=('id','product')


class MyImageAdminForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


# class ProductAdminForm(ModelForm):
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)


class filterCategory(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(filterCategory, self).__init__(*args,**kwargs)
        self.fields['category'].queryset = Category.objects.filter(children=None)


class ProductAdmin(admin.ModelAdmin):
    form =  ProductAdminForm
    prepopulated_fields = {'slug':("title",)}
    list_display= ( 'id','title', 'category', 'price', 'available','get_photo')
    list_display_links=('id','title')
    list_editable=('available',)
    # save_as = True
    # save_on_top = True
    search_fields=('title',)
    change_form_template = 'custom_admin/change_form.html'
    readonly_fields = ('views',)

    # form = filterCategory
    # formfield_overrides = { TreeManyToManyField:{'widget':CheckboxSelectMultiple},}
    def get_photo(self,obj):
        if obj.image1:
            return mark_safe(f'<img src="{obj.image1.url}" width="50">')
        return '-'
    get_photo.short_description = 'Фото'

class SizeInline(admin.TabularInline):
    verbose_name='Размеры'
    model=Size


class SizeAdmin(admin.ModelAdmin):
    inlines = [
        SizeInline,
        ]


class  MPTTModelAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug':("name",)}



admin.site.register(Category,MPTTModelAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product,ProductAdmin)
admin.site.register(Size)
admin.site.register(Rewiews)


admin.site.register(TopText)
admin.site.register( MyTopImage)
admin.site.register(ChangeMyInfo)
admin.site.register(Logo)
admin.site.register(AboutUs,AboutAdmin)
admin.site.register(MyImage)
admin.site.register(ContactUs,ContactsAdmin)
admin.site.register(Delivery,DeliveryAdmin)
admin.site.register(ReturnsItem,ReturnsAdmin)
admin.site.register(Whishlist)

admin.site.site_title="Администрация магазина"
admin.site.site_header="Магазин"
