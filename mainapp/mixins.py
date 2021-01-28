from django.views.generic import View
from .models import Cart,Customer,Product,User



    
class CartMixin(View):
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            if not customer:
                customer= Customer.objects.create(
                    user=request.user
                )
            cart = Cart.objects.filter(owner=customer,in_order=False).first()
            if not cart:
                cart= Cart.objects.create(owner=customer)
        else:
            session_key=request.session.session_key
            name=str(session_key)
            user= User.objects.filter(username=name).first()
            if not user:
                user = User.objects.create_user(name, 'randomemail', 'randomemail')
            customer = Customer.objects.filter(user=user).first()
            if not customer:

                customer= Customer.objects.create(
                    user=user 
                )
          
            cart= Cart.objects.filter(for_anonymoys_user=True,owner=customer,in_order=False).first()
            if not cart:
                cart= Cart.objects.create(for_anonymoys_user=True,owner=customer)
        if cart:
            self.cart=cart
            self.cart.save()
        return super().dispatch(request,*args,**kwargs)
