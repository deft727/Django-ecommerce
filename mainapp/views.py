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
from django.views.generic import DetailView,View,ListView
from .models import Category,Customer,Cart,CartProduct,Product,Order,MyImage,User,MyTopImage,AboutUs,Returns,Delivery,ContactUs,ReturnsItem,Whishlist
from .mixins import CartMixin
from .forms import OrderForm,LoginForm,RegistrationForm,ContactForm,RewiewsForm
from .utils import recalc_cart
from specs.models import ProductFeatures
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator
from django.template.loader import render_to_string,get_template
from datetime import datetime, date, time

from liqpay import LiqPay
from  django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.cache import cache


def custom_404(request):
    return render(request, '404.html', {}, status=404)



class AboutUsView(CartMixin,View):
    def get(self,request,*args,**kwargs):
        about= AboutUs.objects.all()
        context= {
            'about': about,
            'cart':self.cart,
        }
        return render(request,'about.html',context)

class  ContactUsView(CartMixin,View):
    def get(self,request,*args,**kwargs):
        contact= ContactUs.objects.all()
        context= {
            'contact': contact,
            'cart':self.cart,
        }
        return render(request,'contact-us.html',context)


class  DeliveryView(CartMixin,View):
    def get(self,request,*args,**kwargs):
        delivery= Delivery.objects.all()
        context= {
            'delivery': delivery,
            'cart':self.cart,
        }
        return render(request,'delivery.html',context)

class  ReturnsView(CartMixin,View):
    def get(self,request,*args,**kwargs):
        returns= ReturnsItem.objects.all()
        context= {
            'returns': returns,
            'cart':self.cart,
        }
        return render(request,'returns.html',context)


class MyQ(Q):
    default = 'OR'


class BaseView(CartMixin, View):
    def get(self,request,*args,**kwargs):

        Topimage=MyTopImage.objects.all()
        products = Product.objects.all().order_by('-id')[:8]
        # myimage = cache.get('myimage')
        # if not myimage:
        myimage= MyImage.objects.all()
            # cache.set('myimage',myimage,30)
        randomProducts =  Product.objects.all().order_by('?')[:10]
        form= ContactForm(request.POST or None)
        title = 'Сайт'
        context= {
            'title': title ,
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
            email = EmailMessage('Интернет магазин',' ГОСТЬ С ИМЕНЕМ - '+ name+ ' НАПИСАЛ- '+ text + ' ЕГО ПОЧТА ДЛЯ СВЗЯИ: '+ email_user, to=['magikmagazin123@gmail.com'])
            email.send()
            messages.add_message(request,messages.SUCCESS,'Ваше сообщение отправлено')
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.ERROR,'Неверно введена капча')

        return HttpResponseRedirect('/')



class ProductDetailView(CartMixin,DetailView):
    context_object_name='product'
    model= Product
    template_name='product_detail.html'
    slug_url_kwarg='slug'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('search')
        # context['categories'] =  self.get_object().category.__class__.objects.all()
        context['cart']= self.cart
        context['title'] = self.get_object().title
        category=self.get_object().category
        context['randomProducts']= Product.objects.filter(category=category)[:12]
        return context




class CategoryDetailView(CartMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('search')
        query1 = self.request.GET.get('page')
        category = title =self.get_object()
        context['title']=title
        context['cart'] = self.cart
        context['categories'] = self.model.objects.all()
        page_number = self.request.GET.get('page',1) 
        filter_by= self.request.GET.get('sort')
        addSort =''
        if   not query and  not self.request.GET :
            category_man_id = category.id # укажи стартовую верхнюю категорию
            sub1 = list(Category.objects.filter(parent = category_man_id))
            sub2 = list(Category.objects.filter(parent__in = sub1))
            if sub1 or sub2:
                category_products= Product.objects.filter(category__in = sub1+sub2)
            else:
                category_products =  Category.objects.get(id=category.id).get_products()
         
            paginator = Paginator(category_products, 18)  # 3 поста на каждой странице  
            page =paginator.get_page(page_number) 
            context['category_products'] = page
            context['page']= page
            return context
      
        if query1 or filter_by:
            category_man_id = category.id # укажи стартовую верхнюю категорию
            sub1 = list(Category.objects.filter(parent = category_man_id))
            sub2 = list(Category.objects.filter(parent__in = sub1))
            if sub1 or sub2:
                category_products= Product.objects.filter(category__in = sub1+sub2)
            else:
                category_products = Product.objects.filter(category=category)

            if filter_by=='priceup':
                category_products = category_products.order_by('price')
            if filter_by=='pricedown':
                category_products = category_products.order_by('-price')
            if filter_by=='title':
                category_products = category_products.order_by('title')
            if filter_by:

                addSort = '&sort=' + filter_by
            paginator = Paginator(category_products, 18)  # 3 поста на каждой странице  
            page =paginator.get_page(page_number) 
        
            context['addSort']=addSort
            context['category_products'] = page
            context['page']= page
            return context
  
        if query:
            if query[0].lower():
                query= query.title()
            products =   Product.objects.filter(Q(title__icontains=query))
            paginator = Paginator(products, 18)  # 3 поста на каждой странице  
            page =paginator.get_page(page_number) 
            context['category_products'] = page
            context['page']= page
            return context


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
        paginator = Paginator(products, 18)  # 3 поста на каждой странице  
        page =paginator.get_page(page_number) 
        context['category_products'] = page
        context['page']= page
        return context


class AddtoWhishlistView(CartMixin,View):
    def get(self,request,*args,**kwargs):
        page =  kwargs.get('x')
        if request.user.is_authenticated:
            name = request.user
            user = User.objects.filter(username=name).first()
        else:
            name = str(request.session.session_key)
            user=User.objects.filter(username=name).first()
        product_slug= kwargs.get('slug')
        product= Product.objects.get(slug=product_slug)
        try:
            Whishlist.objects.get_or_create(owner=user,products=product)
            messages.add_message(request,messages.SUCCESS,'Товар добавлен в избранноe')
        finally:
            if page == 'index':
                return HttpResponseRedirect("/")
            if page == 'product':
                return HttpResponseRedirect(product.get_absolute_url())
            if page == 'category':
                return HttpResponseRedirect("/category/Men/")


class WhislistView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            name = request.user
            user = User.objects.filter(username=name).first()
        else:
            name = str(request.session.session_key)
            user=User.objects.filter(username=name).first()
        title='Избранное'
        favorite = Whishlist.objects.filter(owner=user)
        return render(request,'whishlist.html',{'title':title,
                'favorite':favorite,'cart':self.cart, })


class DeleteFromWhislist(CartMixin,View):

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            name = request.user
            user = User.objects.filter(username=name).first()
        else:
            name = str(request.session.session_key)
            user=User.objects.filter(username=name).first()
        product_slug=kwargs.get('slug')
        product= Product.objects.get(slug=product_slug)
        try:
            delete= Whishlist.objects.get(owner=user,products=product).delete()
        except:
            return HttpResponseRedirect('/whishlist/')
            
        messages.add_message(request,messages.INFO,'Товар удален из избранного')
        return HttpResponseRedirect('/whishlist/')



class AddToCartView(CartMixin,View):

    def get(self,request,*args,**kwargs):
        
        product_slug= kwargs.get('slug')
        product= Product.objects.get(slug=product_slug)
        qty= int(request.GET.get('qty'))
        size = request.GET.get('size')
        if size:
            cart_product,created=CartProduct.objects.get_or_create(
                user=self.cart.owner,cart=self.cart,product=product,size=size
                )
        else:
            messages.add_message(request,messages.INFO,'Выберите размер')
            return redirect(product.get_absolute_url())

        if created and qty >= 1:
            cart_product.qty= qty
            cart_product.save()
            self.cart.products.add(cart_product)
            messages.add_message(request,messages.SUCCESS,'Товар добавлен в корзину')

        else:
            messages.add_message(request,messages.ERROR,'Товар уже в корзине')

        recalc_cart(self.cart)
        return redirect(product.get_absolute_url())


class DeleteFomCartView(CartMixin,View):

    def get(self,request,*args,**kwargs):
        product_slug=kwargs.get('slug')
        size= kwargs.get('size')
        product= Product.objects.get(slug=product_slug)
        try:
            cart_product=CartProduct.objects.get(
            user=self.cart.owner,cart=self.cart,product=product,size=size
        )
        except:
            return HttpResponseRedirect('/cart/')
            
        self.cart.products.remove(cart_product)
        cart_product.delete()
        recalc_cart(self.cart)
        messages.add_message(request,messages.INFO,'Товар Удален')
        return HttpResponseRedirect('/cart/')


class ChangeQTYView(CartMixin,View):
    def post(self,request,*args,**kwargs):
        product_slug= kwargs.get('slug')
        qty = request.POST.get('qty').split('/')[0]
        size = request.POST.get('qty').split('/')[1]
        product= Product.objects.get(slug=product_slug)
        cart_product=CartProduct.objects.filter(
            user=self.cart.owner,cart=self.cart,product=product,size=size
        ).first()
        if qty =='1':
            cart_product.qty+=1
            cart_product.save()
            recalc_cart(self.cart)

        else:
            cart_product.qty-=1
            cart_product.save()
            recalc_cart(self.cart)

        messages.add_message(request,messages.INFO,'Кол-во изменено')
        return HttpResponseRedirect('/cart/')


class CartView(CartMixin, View):
    def get(self, request, *args, **kwargs):

        # category = Category.objects.all()
        title='Корзина'
        context = {
            'title':title,
            'cart': self.cart,
            # 'category': category
        }
        return render(request, 'cart.html', context)


class CheckoutView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        # category = Category.objects.all()
        form=OrderForm(request.POST or None)
        title='Оформление заказа'
        context = {
            'title':title,
            'cart': self.cart,
            # 'category': category,
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
            orders = Order.objects.filter(customer=customer).order_by('-id')[:1]



        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.phone = form.cleaned_data['phone']

            phone=form.cleaned_data['phone']

            new_order.first_name = form.cleaned_data['first_name']

            name=form.cleaned_data['first_name']

            new_order.last_name = form.cleaned_data['last_name']
            new_order.adress = form.cleaned_data['adress']

            adress=form.cleaned_data['adress']

            new_order.email=form.cleaned_data['email']
            email = form.cleaned_data['email']

            new_order.otdel = form.cleaned_data['otdel']
            new_order.buying_type = form.cleaned_data['buying_type']
            new_order.comment = form.cleaned_data['comment']
            new_order.status_pay = 'nal'
            comment=form.cleaned_data['comment']
            payment = request.POST.get('payment')
            if payment == 'online':
                new_order.status_pay = 'wait'
                new_order.save()
                self.cart.in_order = True
                self.cart.save()
                new_order.cart = self.cart
                new_order.save()
                customer.orders.add(new_order)
                
                return redirect ('/pay/')

            
            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            new_order.save()
            customer.orders.add(new_order)
            orders = Order.objects.filter(customer=customer).order_by('-id')[:1]
# -----------------------------------------------------------------------------------------------------------------------
            subject = "Заказ на сайте 12312312"
            to = [email,]
            from_email = 'test@example.com'
            ctx = {
                'orders': orders,
            }
            message = get_template('message.html').render(ctx)
            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()
# ----------------------------------------------------------------------------------------------------------------------


            messages.add_message(request, messages.INFO, 'Спасибо за заказ! Менеджер с Вами свяжется')
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/checkout/')

class PayView(TemplateView):
    template_name = 'pay.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.get(user=request.user)
        else:
            session_key=request.session.session_key
            name=str(session_key)
            user= User.objects.filter(username=name).first()
            customer = Customer.objects.filter(user=user).first()
        orders = Order.objects.filter(customer=customer).order_by('-id')[:1].first()
        # /
        if orders:
            liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
            params = {
                'action': 'pay',
                'amount': int(orders.cart.final_price) ,
                'currency': 'UAH',
                'description': 'Payment for clothes',
                'version': '3',
                'order_id':  orders.id ,
                'sandbox': 0, # sandbox mode, set to 1 to enable it
                'result_url':'https://mysite123456.herokuapp.com/',
                'server_url': 'https://mysite123456.herokuapp.com/pay-callback/', # url to callback view
            }
            signature = liqpay.cnb_signature(params)
            data = liqpay.cnb_data(params)
            return render(request, self.template_name, {'signature': signature, 'data': data})
        else:
            return HttpResponseRedirect('/')


@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        # if sign == signature:
        response =liqpay.decode_data_from_str(data)
        try:
            phone = response['sender_phone']
        except:
            phone = '0'
        if phone != '0' and signature == sign:
            orders = Order.objects.get(id=response['order_id'])
            if response['status'] == 'success':
                orders.status_pay = 'pay'
                orders.save()
                x ='сумма платежа'+str(response['amount'])+ '... response order id==='+response['order_id']+'--status----'+response['status'] +'--phone'+phone +'Остальное -------'+str(response)
                send_mail('Платеж удачен!',x, "Yasoob",['zarj09@gmail.com'], fail_silently=False)
            if response['status'] == 'failed':
                orders.status_pay='not_pay'
                orders.save()
                # x = '... response order id==='+response['order_id']+'--status----'+response['status'] +'--phone'+phone +'Остальное -------'+str(response)
                send_mail('Платеж отклонен!', "Yasoob",['zarj09@gmail.com'], fail_silently=False)
            if response['status'] == 'reversed':
                orders.status_pay='reversed'
                orders.save()
                # x = '... response order id==='+response['order_id']+'--status----'+response['status'] +'--phone'+phone +'Остальное -------'+str(response)
                send_mail('Платеж возвращн', "Yasoob",['zarj09@gmail.com'], fail_silently=False)
            if response['status'] == 'error':
                orders.status_pay = 'miss'
                orders.save()
                #написать если ошибка при оплате
                # x = ' ошибка при оплате '+' .order id==='+response['order_id']+'--status----'+response['status'] +'--phone'+phone +'Остальное -------'+str(response)
                send_mail('Платеж ошибка!', "Yasoob",['zarj09@gmail.com'], fail_silently=False)


        result_url = 'https://mysite123456.herokuapp.com/'
        return HttpResponse()
# otzivy
class ProductRewiew(View):
    def post(self,request,pk):
        form = RewiewsForm(request.POST or None)
        product=Product.objects.get(id=pk)
        if form.is_valid():
            form=form.save(commit=False)
            form.name= request.user
            form.product= product
            form.save()
            messages.add_message(request,messages.INFO,'Ваш отзыв добавлен!')
        return redirect(product.get_absolute_url())


class LoginView(CartMixin,View):
    def get(self,request,*args,**kwargs):
        if  request.user.is_authenticated:
            messages.add_message(request,messages.ERROR,'Вы уже залогинены')
            return redirect('base')
        form = LoginForm(request.POST or None)
        # category = Category.objects.all()
        title = 'Логин'
        context= {'title':title,
        'form':form,
        #  'category':category,
        'cart':self.cart}
        return render(request,'login.html',context)


    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST or None)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            if '@' in username:
                user1= User.objects.filter(email=username).first()
                user= authenticate(username=user1,password=password)
            else:
                user= authenticate(username=username,password=password)
            if user:
                login(request,user)
            return HttpResponseRedirect('/')
        context={'form':form,'cart':self.cart}
        return render(request,'login.html',context)

# registration
class RegistrationView(CartMixin,View):
    def get(self,request,*args,**kwargs):
        if  request.user.is_authenticated:
            messages.add_message(request,messages.ERROR,'Вы уже зарегистрированы')
            return redirect('base')
        form=RegistrationForm(request.POST or None)
        # categories=Category.objects.all()
        title = 'Регистрация'
        context = {
            'title':title,
            'form':form,
            # 'categories':categories,
            'cart':self.cart
        }
        return render(request,'registration.html',context)
    
    def post(self,request,*args,**kwargs):
        form= RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.username=form.cleaned_data['username']
            new_user.email=form.cleaned_data['email']
            new_user.first_name=form.cleaned_data['first_name']
            new_user.last_name=form.cleaned_data['last_name']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            oldname = request.session.session_key
            oldorders = Order.objects.filter(customer__user__username=oldname)
            customer = Customer.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                adress=form.cleaned_data['adress'],
            )
            customer.save()

            if oldorders:
                customer.orders.set(oldorders)
                for i in oldorders:
                    i.customer = customer
                    i.customer.save()
                    i.save()
                
                # User.objects.filter(username=oldname).delete()
                
            user= authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            login(request,user)
            messages.add_message(request,messages.SUCCESS,'Вы успешно зарегистрировались на сайте')
            return redirect('base')
        else:
            messages.add_message(request,messages.ERROR,'Ошибка регистрации')
        context={'form':form,'cart':self.cart}
        return render(request,'registration.html',context)


class ProfileView(CartMixin,View):
    def get (self,request,*args,**kwargs):
        if not  request.user.is_authenticated:
            messages.add_message(request,messages.ERROR,'Для просмотра заказов и их статуса зарегистрируйтесь')
            return redirect('registration')
        customer = Customer.objects.get(user=request.user)
        orders= Order.objects.filter(customer=customer).order_by('-created_at')
        title = 'Профиль '+request.user.username

        return render(request,'profile.html',{'title':title,
        'orders':orders,
        'cart':self.cart,
 })

