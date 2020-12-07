from django.views.generic import View

from .models import Cart,Customer,Product




# class CategoryDeatailMixin(SingleObjectMixin):

#     def get_context_data(self,**kwargs):
#         if isinstance(self.get_object(),Category):
#             model= self.CATEGOTY_SLUG2PRODUCT_MODEL[self.get_object().slug]
#             context= super().get_context_data(**kwargs)
#             context['categories'] = Category.objects.get_categories_for_top()
#             context['category_products'] = model.objects.all()
#             return context

#         context= super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.get_categories_for_top()
#         return context
    
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
            cart= Cart.objects.filter(for_anonymoys_user=True).first()
            if not cart:
                cart= Cart.objects.create(for_anonymoys_user=True)
        self.cart=cart
        self.cart.save()
        return super().dispatch(request,*args,**kwargs)
