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



class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = '__all__'


class ReviewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Rewiews
        fields = '__all__'


class RewiewsAdmin(admin.ModelAdmin):
    form = ReviewsAdminForm
    list_display= ( 'id','name','product')
    list_display_links=('id','product')


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
    form = PostAdminForm
    # search_fields= ('title',)
    list_display= ( 'id','title', 'category', 'price', 'available')
    list_display_links=('id','title')
    list_editable=('available',)
    change_form_template = 'custom_admin/change_form.html'
    # form = filterCategory
    # formfield_overrides = { TreeManyToManyField:{'widget':CheckboxSelectMultiple},}


class SizeInline(admin.TabularInline):
    verbose_name='Размеры'
    model=Size


class SizeAdmin(admin.ModelAdmin):
    inlines = [
        SizeInline,
        ]





admin.site.register(Category,MPTTModelAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product,ProductAdmin)
admin.site.register(Size)
admin.site.register(Rewiews,RewiewsAdmin)


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
