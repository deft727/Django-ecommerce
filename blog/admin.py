
from django.contrib import admin
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("title",)}
    form = PostAdminForm
    list_display= ( 'id','title',)
    list_display_links=('id','title')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':("title",)}





admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post,PostAdmin)