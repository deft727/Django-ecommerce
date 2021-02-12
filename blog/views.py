from django.shortcuts import render
from  mainapp.mixins import CartMixin
from django.http import HttpResponse
from django.views.generic import DetailView,View,ListView


class IndexBlog(CartMixin,View):
    def get(self,request,*args,**kwargs):
        context= {
            'cart':self.cart,
                }
        return render(request,'blog-list.html',context)


class BlogDetail(CartMixin,View):
    def get(self,request,*args,**kwargs):
        context= {
            'cart':self.cart,
                }
        return render(request,'blog-detail.html',context)