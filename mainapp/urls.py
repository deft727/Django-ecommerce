from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.decorators.cache import cache_page

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
                    ContactUsView,
                    DeliveryView,
                    ReturnsView,
                    AddtoWhishlistView,
                    WhislistView,
                    DeleteFromWhislist,
                    PayView, 
                    PayCallbackView
                    )
from django.contrib.auth import views as authViews
# from django.conf.urls import url
from django.conf.urls import url
import re

# handler404 = 'mainapp.views.custom_page_not_found_view'

urlpatterns = [
    path('',cache_page(30)(BaseView.as_view()),name='base'),
    path('products/<str:slug>/',cache_page(30)(ProductDetailView.as_view()),name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/',CartView.as_view(),name='cart'),

    path('add-to-cart/<str:slug>/',AddToCartView.as_view(),name='add_to_cart'),

    path('remove-from-cart/<str:slug>/<str:size>/',DeleteFomCartView.as_view(),name='remove_from_cart'),
    path('change-qty/<str:slug>/',ChangeQTYView.as_view(),name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('login/',LoginView.as_view(), name='login'),
        path('pass-reset/',authViews.PasswordResetView.as_view(template_name="pass-reset.html"),name="pass-reset"),
    path('passwod_reset_confirm/<uidb64>/<token>/',authViews.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name="password_reset_confirm"),
        path('passwod-reset/done/',authViews.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),
    path('reset_password_complete/', authViews.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),
    path('logout/',LogoutView.as_view(next_page="/"), name='logout'),
    path('registration/',RegistrationView.as_view(), name='registration'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('review/<int:pk>/', ProductRewiew.as_view(),name="add_review"),
    path('about/', AboutUsView.as_view(), name='about'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('delivery/', DeliveryView.as_view(), name='delivery'),
    path('returns/', ReturnsView.as_view(), name='returns'),
    path('add-to-whishlist/<str:slug>/<str:x>/',AddtoWhishlistView.as_view(),name='add_to_whishlist'),
    path('whishlist/', WhislistView.as_view(),name='whishlist'),
    path('remove_from_whishlist/<str:slug>/', DeleteFromWhislist.as_view(),name='remove_from_whishlist'),

    # path('pay/',PayView.as_view(), name='pay_view'),
    # path('pay-callback/', PayCallbackView.as_view(), name='pay_callback'),
    # url(r'^$',BaseView.as_view(),name='base'),
    url(r'^pay/$', PayView.as_view(), name='pay_view'),
    url(r'^pay-callback/$', PayCallbackView.as_view(), name='pay_callback'),
]             

custom_404 = 'mainapp.views.custom_404'
