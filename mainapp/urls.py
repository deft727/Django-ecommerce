from django.urls import path
from django.contrib.auth.views import LogoutView
# from . import views
from .views import (
    # HtmlView,
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
                    ProductRewiew)



urlpatterns = [
    # path('',HtmlView().as_view(),name='HtmlView'),
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
]

