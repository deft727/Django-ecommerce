from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
                    BaseView,
                    ProductDetailView,
                    CategoryDetailView,
                    CartView,
                    AddToCartView,
                    DeleteFomCartView,
                    ChangeQTYView,
                    CheckoutView,
                    MakeOrderView,
                    LoginView,
                    RegistrationView,
                    ProfileView,
                    ProductRewiew,
                    AboutUsView,
                    custom_404,
                    )
# from django.conf.urls import url



# handler404 = 'mainapp.views.custom_page_not_found_view'

urlpatterns = [
    path('',BaseView.as_view(),name='base'),
    path('products/<str:slug>/',ProductDetailView.as_view(),name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/',CartView.as_view(),name='cart'),
    path('add-to-cart/<str:slug>/',AddToCartView.as_view(),name='add_to_cart'),
    path('remove-from-cart/<str:slug>/',DeleteFomCartView.as_view(),name='remove_from_cart'),
    path('change-qty/<str:slug>/',ChangeQTYView.as_view(),name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page="/"), name='logout'),
    path('registration/',RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('review/<int:pk>/', ProductRewiew.as_view(),name="add_review"),
    path('about/', AboutUsView.as_view(), name='about'),
    # url(r'^$',BaseView.as_view(),name='base'),
]

custom_404 = 'mainapp.views.custom_404'
