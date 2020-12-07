from decimal import Decimal
from unittest import mock
from django.test import TestCase,RequestFactory
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category,Book,Smart,Cart,CartProduct,Customer
from .views import recalc_cart,AddToCartView,BaseView


User= get_user_model()

class ShopTestCases(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser',password='password')
        self.category=Category.objects.create(name='book',slug='book')
        image = SimpleUploadedFile("book_image.jpg", content=b'', content_type="image/jpg")
        self.book = Book.objects.create(
            category=self.category,
            title="test-slug",
            slug="test-slug",
            image=image,
            price=Decimal('5000.00'),
            diagonal='123',
            size='123'
        )
        self.customer = Customer.objects.create(user=self.user,phone='123123',adress='asdagevsdscv')
        self.cart = Cart.objects.create(owner=self.customer)
        self.cart_product= CartProduct.objects.create(
            user=self.customer,
            cart= self.cart,
            content_object= self.book
        )

    def test_add_to_cart(self):
        self.cart.products.add(self.cart_product)
        recalc_cart(self.cart)
        self.assertIn(self.cart_product,self.cart.products.all())
        self.assertEqual(self.cart.products.count(),1)
        self.assertEqual(self.cart.final_price,Decimal('5000.00'))

    def test_response_form_add_to_cart_view(self):
        factory = RequestFactory()   
        request=factory.get('')
        request.user = self.user    
        response= AddToCartView.as_view()(request,ct_model="book",slug="test-slug") 
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,'/cart/')

    def test_mock(self):
        mock_data = mock.Mock(status_code=444)
        with mock.patch('mainapp.views.BaseView.get', return_value = mock_data) as mock_data_:
            factory= RequestFactory()
            request = factory.get('')
            request.user= self.user
            response= BaseView.as_view()(request)
            self.assertEqual(response.status_code,444)
