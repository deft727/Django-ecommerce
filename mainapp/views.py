
import operator
from functools import reduce
from itertools import chain
from django.db import transaction
from django.db.models import Q

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.views.generic import DetailView,View
from .models import Category,Customer,Cart,CartProduct,Product,Order,MyImage,User,MyTopImage
from .mixins import CartMixin
from .forms import OrderForm,LoginForm,RegistrationForm,ContactForm,RewiewsForm
from .utils import recalc_cart

from specs.models import ProductFeatures
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sessions.models import Session

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  

# def user_logged_in_handler(sender, request, user, **kwargs)
# UserSession.objects.get_or_create(user = user, session_id = request.session.session_key)
# user_logged_in.connect(user_logged_in_handler)


def send_email(email,name,phone,comment):
    email = EmailMessage('Интернет магазин', name+ 'вы сделали заказ '+comment+'ваш телдля связи'+phone, to=[email])
    email.send()


class MyQ(Q):
    default = 'OR'


class BaseView(CartMixin, View):
    def get(self,request,*args,**kwargs):

        # if not request.session.session_key:
        #     request.session.create()
        
        # session_id = request.session.session_key

        # print(User.objects.filter(username='session_key').first())



        Topimage=MyTopImage.objects.all()
        category = Category.objects.all()
        products = Product.objects.all().order_by('-id')[:8]
        myimage= MyImage.objects.all()
        randomProducts= Product.objects.all().order_by('?')[:10]
        form= ContactForm(request.POST or None)


        context= {
            
            'category': category,
            'products' : products,
            'cart':self.cart,
            'Topimage':Topimage,
            'myimage':myimage,
            'randomProducts':randomProducts,
            'form':form
        }
        return render(request,'index.html',context)


    def post(self,request,*args,**kwargs):

        form= ContactForm(request.POST or None)
        if form.is_valid():
            name= form.cleaned_data['name']
            email_user = form.cleaned_data['email']
            text= form.cleaned_data['text']
            email = EmailMessage('Интернет магазин','ГОСТЬ С ИМЕНЕМ - '+ name+ ' НАПИСАЛ- '+ text + ' ЕГО ПОЧТА ДЛЯ СВЗЯИ: '+ email_user, to=['magikmagazin123@gmail.com'])
            email.send()
            messages.add_message(request,messages.INFO,'Ваше сообщение отправлено')
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')



class ProductDetailView(CartMixin,DetailView):
    context_object_name='product'
    model= Product
    template_name='product_detail.html'
    slug_url_kwarg='slug'
    # cart_product_form=CartAddProductForm()
   
    def get_context_data(self,**kwargs):
        # slug= kwargs.get('slug')
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_object().category.__class__.objects.all()
        context['cart']= self.cart
        context['randomProducts']= Product.objects.all().order_by('?')[:10]
        return context





class CategoryDetailView(CartMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('search')
        query1 = self.request.GET.get('page')
        print(query,query1)
        category = self.get_object()
        context['cart'] = self.cart
        context['categories'] = self.model.objects.all()

        page_number = self.request.GET.get('page',1) 
        # if page is None:
        #     page=1
        print(page_number)

        if   not query and  not self.request.GET :
            category_products = Product.objects.filter(category=category)
            # context['category_products'] = category_products
            print(self.request.GET.get('page'))
            paginator = Paginator(category_products, 1)  # 3 поста на каждой странице  
            page =paginator.get_page(page_number) 
            print(page)
            # try:  
            #     posts = paginator.page(page)  
            # except PageNotAnInteger:  
            #     # Если страница не является целым числом, поставим первую страницу  
            #     posts = paginator.page(1)  
            # except EmptyPage:  
            #     # Если страница больше максимальной, доставить последнюю страницу результатов  
            #     posts = paginator.page(paginator.num_pages)
            context['category_products'] = page
            context['page']= page
            return context

        if query1:
            category_products = Product.objects.filter(category=category)
            # context['category_products'] = category_products
            print(self.request.GET.get('page'))
            paginator = Paginator(category_products, 1)  # 3 поста на каждой странице  
            page =paginator.get_page(page_number) 
            print(page)
            # try:  
            #     posts = paginator.page(page)  
            # except PageNotAnInteger:  
            #     # Если страница не является целым числом, поставим первую страницу  
            #     posts = paginator.page(1)  
            # except EmptyPage:  
            #     # Если страница больше максимальной, доставить последнюю страницу результатов  
            #     posts = paginator.page(paginator.num_pages)
            context['category_products'] = page
            context['page']= page
            return context


        if query:
            # products= Product.objects.filter(category=category)
            products = category.product_set.filter(Q(title__icontains=query))
            paginator = Paginator(products, 2)  # 3 поста на каждой странице  
            page =paginator.get_page(page_number) 
            print('query',page)
            context['category_products'] =page
            context['page']= page

            return context




        # if category_products:
        #     paginator = Paginator(category_products, 3)  # 3 поста на каждой странице  
        #     page = request.GET.get('page') 

        #     try:  
        #         posts = paginator.page(page)  
        #     except PageNotAnInteger:  
        #         # Если страница не является целым числом, поставим первую страницу  
        #         posts = paginator.page(1)  
        #     except EmptyPage:  
        #         # Если страница больше максимальной, доставить последнюю страницу результатов  
        #         posts = paginator.page(paginator.num_pages)
        #     return 		  {'context':context,
        #                     'page': page,  
		#                    'posts': posts} 



        url_kwargs = {}
        for item in self.request.GET:
            if len(self.request.GET.getlist(item)) > 1:
                url_kwargs[item] = self.request.GET.getlist(item)
            else:
                url_kwargs[item] = self.request.GET.get(item)
        q_condition_queries = Q()
        for key, value in url_kwargs.items():
            if isinstance(value, list):
                q_condition_queries.add(Q(**{'value__in': value}), Q.OR)
            else:
                q_condition_queries.add(Q(**{'value': value}), Q.OR)
        pf = ProductFeatures.objects.filter(
            q_condition_queries
        ).prefetch_related('product', 'feature').values('product_id')
        products = Product.objects.filter(id__in=[pf_['product_id'] for pf_ in pf])
        # context['category_products'] = products

        paginator = Paginator(products, 2)  # 3 поста на каждой странице  
        page =paginator.get_page(page_number) 
        print('filter',page)
        context['category_products'] = page
        context['page']= page
        return context





class AddToCartView(CartMixin,View):
    def get(self,request,*args,**kwargs):

        product_slug= kwargs.get('slug')
        product= Product.objects.get(slug=product_slug)


        cart_product,created=CartProduct.objects.get_or_create(
            user=self.cart.owner,cart=self.cart,product=product
        )
        if created:
            self.cart.products.add(cart_product)
        recalc_cart(self.cart)
        messages.add_message(request,messages.INFO,'Товар добавлен в корзину')
        return redirect(product.get_absolute_url())



class DeleteFomCartView(CartMixin,View):

    def get(self,request,*args,**kwargs):

        product_slug=kwargs.get('slug')
        product= Product.objects.get(slug=product_slug)
        cart_product=CartProduct.objects.get(
            user=self.cart.owner,cart=self.cart,product=product
        )
        self.cart.products.remove(cart_product)
        cart_product.delete()
        recalc_cart(self.cart)
        messages.add_message(request,messages.INFO,'Товар Удален')
        return HttpResponseRedirect('/cart/')


class ChangeQTYView(CartMixin,View):
    def post(self,request,*args,**kwargs):
        
        product_slug= kwargs.get('slug')
        product= Product.objects.get(slug=product_slug)
        cart_product=CartProduct.objects.get(
            user=self.cart.owner,cart=self.cart,product=product
        )
        if request.POST.get('qty')=='1':
            cart_product.qty+=1
            cart_product.save()
            recalc_cart(self.cart)
        if request.POST.get('qty')=='0':
            cart_product.qty-=1
            cart_product.save()
            recalc_cart(self.cart)

        messages.add_message(request,messages.INFO,'Кол-во изменено')
        return HttpResponseRedirect('/cart/')


class CartView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        context = {
            'cart': self.cart,
            'category': category
        }
        return render(request, 'cart.html', context)


class CheckoutView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        form=OrderForm(request.POST or None)
        context = {
            'cart': self.cart,
            'category': category,
            'form': form
        }
        return render(request, 'checkout.html', context)

class MakeOrderView(CartMixin,View):
    
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        if request.user.is_authenticated:
            customer = Customer.objects.get(user=request.user)
        else:
            session_key=request.session.session_key
            name=str(session_key)
            user= User.objects.filter(username=name).first()
            customer = Customer.objects.filter(user=user).first()



        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.phone = form.cleaned_data['phone']

            phone=form.cleaned_data['phone']

            new_order.first_name = form.cleaned_data['first_name']

            name=form.cleaned_data['first_name']

            new_order.last_name = form.cleaned_data['last_name']
            new_order.adress = form.cleaned_data['adress']

            email=form.cleaned_data['adress']


            new_order.otdel = form.cleaned_data['otdel']
            new_order.buying_type = form.cleaned_data['buying_type']
            new_order.comment = form.cleaned_data['comment']

            comment=form.cleaned_data['comment']

            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            new_order.save()
            customer.orders.add(new_order)


            # email=form.cleaned_data['adress']
            # print(email)
            # name= form.cleaned_data['first_name']
            # body= form.cleaned_data['phone']
            send_email(email,name,phone,comment)

            messages.add_message(request, messages.INFO, 'Спасибо за заказ! Менеджер с Вами свяжется')
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/checkout/')


# otzivy
class ProductRewiew(View):
    def post(self,request,pk):
        form = RewiewsForm(request.POST or None)
        product=Product.objects.get(id=pk)
        # print(product)
        if form.is_valid():
            form=form.save(commit=False)
            form.name= request.user
            form.product= product
            form.save()
            messages.add_message(request,messages.INFO,'Ваш отзвы добавлен!')
        return redirect(product.get_absolute_url())


class LoginView(CartMixin,View):
    def get(self,request,*args,**kwargs):
        form = LoginForm(request.POST or None)
        category = Category.objects.all()
        context= {'form':form, 'category':category,'cart':self.cart}
        return render(request,'login.html',context)

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST or None)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect('/')
        context={'form':form,'cart':self.cart}
        return render(request,'login.html',context)

class RegistrationView(CartMixin,View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST or None)
        categories=Category.objects.all()
        context = {
            'form':form,'categories':categories,'cart':self.cart
        }
        return render(request,'registration.html',context)
    
    def post(self,request,*args,**kwargs):
        form= RegistrationForm(request.POST or None)
        if form.is_valid():
            # print('Эмайл тут   ',form.cleaned_data)
            new_user=form.save(commit=False)
            new_user.username=form.cleaned_data['username']
            new_user.email=form.cleaned_data['email']
            # print(form.cleaned_data['email'])
            new_user.first_name=form.cleaned_data['first_name']
            new_user.last_name=form.cleaned_data['last_name']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Customer.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                adress=form.cleaned_data['adress']
            )
            user= authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            login(request,user)
            return  HttpResponseRedirect('/')
        context={'form':form,'cart':self.cart}
        return render(request,'registration.html',context)


class ProfileView(CartMixin,View):
    def get (self,request,*args,**kwargs):
        customer = Customer.objects.get(user=request.user)
        orders= Order.objects.filter(customer=customer).order_by('-created_at')
        categories= Category.objects.all()
        return render(request,'profile.html',{'orders':orders,'cart':self.cart, 'categories':categories})

