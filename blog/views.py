from django.shortcuts import render
from  mainapp.mixins import CartMixin
from django.http import HttpResponse
from django.views.generic import DetailView,View,ListView
from .models import *


class IndexBlog(CartMixin,ListView):
    model= Post
    template_name = 'blog-list.html'
    context_object_name = 'posts'
    paginate_by = 3
    
    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['cart']=self.cart
        return context


class PostsByCategory(ListView):
    model = Category
    template_name = 'blog-list.html'
    context_object_name = 'posts'
    paginate_by = 1
    allow_empty = False


    def get_queryset(self):
        return Post.objects.filter(category__slug = self.kwargs['slug'])


    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context



class BlogDetail(CartMixin,View):
    def get(self,request,*args,**kwargs):
        context= {
            'cart':self.cart,
                }
        return render(request,'blog-detail.html',context)
