
from django.contrib import admin
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe

class PostAdminForm(forms.ModelForm):
    
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("title",)}
    form = PostAdminForm
    list_display= ( 'id','title','category','created_at','get_photo')
    list_display_links=('id','title')
    save_as = True
    save_on_top = True
    search_fields=('title',)
    list_filter = ('category',)
    readonly_fields = ('views','created_at','get_photo')
    fields = ('title','slug','category','author','tags','content','photo','get_photo','views','created_at')



    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'
    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("title",)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post,PostAdmin)