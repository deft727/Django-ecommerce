from django.shortcuts import render
from  mainapp.mixins import CartMixin
from django.http import HttpResponse
from django.views.generic import DetailView,View,ListView
from .models import *
from django.db.models import F

class IndexBlog(CartMixin,ListView):
    model= Post
    template_name = 'blog-grid.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['cart']=self.cart
        return context


class PostsByCategory(ListView):
    model = Category
    template_name = 'blog-grid.html'
    context_object_name = 'posts'
    paginate_by = 6
    allow_empty = False


    def get_queryset(self):
        return Post.objects.filter(category__slug = self.kwargs['slug'])


    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория блога: '+ str(Category.objects.get(slug=self.kwargs['slug']))
        return context

class PostsByTag(CartMixin,ListView):
    template_name = 'blog-grid.html'
    context_object_name = 'posts'
    paginate_by = 6
    allow_empty = False 


    def get_queryset(self):
        return Post.objects.filter(tags__slug = self.kwargs['slug'])


    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: '+ str(Tag.objects.get(slug=self.kwargs['slug']))
        context['cart']=self.cart
        return context

class BlogDetail(CartMixin,DetailView):
    model = Post
    template_name = 'blog-detail.html'
    context_object_name = 'post'

    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        context['cart']=self.cart
        return context