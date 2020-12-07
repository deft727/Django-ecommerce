import sys
from PIL import Image
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils import timezone
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


User=get_user_model()



class Category(models.Model):

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=250,verbose_name='Для кого')
    brand = models.CharField(max_length=250,verbose_name='Категория')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug': self.slug})

    def get_fields_for_filte_in_template(self):
        return ProductFeatures.objects.filter(
            category=self,
            use_in_filter=True
        ).prefetch_related('category').value('feature_key','feature_,measure','feature_name','filter_type')








class Product(models.Model):

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=250,verbose_name='Наименоватние продукта')
    slug=models.SlugField(unique=True)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    image5 = models.ImageField()

    description = models.TextField(verbose_name='Описание товара',null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена')

    def __str__(self):
        return self.title


    def get_model_name(self):
        return self.__class__.__name__.lower()

    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'slug':self.slug})


    def save(self,*args,**kwargs):

        image1=self.image1
        img1=Image.open(image1)
        new_img1=img1.convert('RGB')
        res_img1=new_img1.resize((800,800),Image.ANTIALIAS)
        filestream= BytesIO()
        file_=res_img1.save(filestream,'JPEG',quality=90)
        filestream.seek(0)
        name= '.'.format(*self.image1.name.split('.'))
        self.image1 = InMemoryUploadedFile(
            filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
        )
        super().save(*args,**kwargs)
        
        image2=self.image2
        img2=Image.open(image2)
        new_img2=img2.convert('RGB')
        res_img2=new_img2.resize((800,800),Image.ANTIALIAS)
        filestream= BytesIO()
        file_=res_img2.save(filestream,'JPEG',quality=90)
        filestream.seek(0)
        name= '.'.format(*self.image2.name.split('.'))
        self.image2 = InMemoryUploadedFile(
            filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
        )
        super().save(*args,**kwargs)

        image3=self.image3
        img3=Image.open(image3)
        new_img3=img3.convert('RGB')
        res_img3=new_img3.resize((800,800),Image.ANTIALIAS)
        filestream= BytesIO()
        file_=res_img3.save(filestream,'JPEG',quality=90)
        filestream.seek(0)
        name= '.'.format(*self.image3.name.split('.'))
        self.image3 = InMemoryUploadedFile(
            filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
        )
        super().save(*args,**kwargs)

        image4=self.image4
        img4=Image.open(image4)
        new_img4=img4.convert('RGB')
        res_img4=new_img4.resize((800,800),Image.ANTIALIAS)
        filestream= BytesIO()
        file_=res_img4.save(filestream,'JPEG',quality=90)
        filestream.seek(0)
        name= '.'.format(*self.image4.name.split('.'))
        self.image4 = InMemoryUploadedFile(
            filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
        )
        super().save(*args,**kwargs)
            
        image5=self.image5
        img5=Image.open(image5)
        new_img5=img5.convert('RGB')
        res_img5=new_img5.resize((800,800),Image.ANTIALIAS)
        filestream= BytesIO()
        file_=res_img5.save(filestream,'JPEG',quality=90)
        filestream.seek(0)
        name= '.'.format(*self.image5.name.split('.'))
        self.image5 = InMemoryUploadedFile(
            filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
        )
        super().save(*args,**kwargs)

    



class MyImage(models.Model):
    title=models.CharField(max_length=50,verbose_name='Описание',null=True,blank=True)
    imagetop1=models.ImageField()
    imagetop2=models.ImageField()

    imagedown1=models.ImageField()
    imagedown2= models.ImageField()

    def save(self,*args,**kwargs):
        imagedown1=self.imagedown1
        img=Image.open(imagedown1)
        new_img=img.convert('RGB')
        res_img=new_img.resize((958,401),Image.ANTIALIAS)
        filestream= BytesIO()
        file_=res_img.save(filestream,'JPEG',quality=90)
        filestream.seek(0)
        name= '.'.format(*self.imagedown1.name.split('.'))
        self.imagedown1 = InMemoryUploadedFile(
            filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
        )
        super().save(*args,**kwargs)

        imagedown2=self.imagedown2
        img=Image.open(imagedown2)
        new_img=img.convert('RGB')
        res_img=new_img.resize((960,401),Image.ANTIALIAS)
        filestream= BytesIO()
        file_=res_img.save(filestream,'JPEG',quality=90)
        filestream.seek(0)
        name= '.'.format(*self.imagedown2.name.split('.'))
        self.imagedown2 = InMemoryUploadedFile(
            filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
        )
        super().save(*args,**kwargs)






class ProductFeatures(models.Model):
     
    RADIO='radio'
    CHECKBOX='checkbox'
    FILTER_TYPE_CHOICES=(
        (RADIO,'Радиокнопка'),
        (CHECKBOX,'Чекбокс')
    )
    feature_key = models.CharField(max_length=100,verbose_name='Ключ характеристики')
    feature_name= models.CharField(max_length=255,verbose_name='Наименование характеристики')
    category= models.ForeignKey(Category,verbose_name='Категория',on_delete=models.CASCADE)
    postfix_for_value= models.CharField(
        max_length=25,
        null=True,
        blank=True,
        verbose_name='Постфикс для значения',
        help_text=f'Для хар-к можно добавить постфикс'
    )
    use_in_filter=models.CharField(max_length=50,
        default=False,
        verbose_name='Использовать фильтрацию товаров на странице'
    )
    filter_type = models.CharField(
        max_length=20,
        verbose_name='Тип фильтра',
        default=CHECKBOX,
        choices=FILTER_TYPE_CHOICES
    )
    filter_measures=models.CharField(
        max_length=50,
        verbose_name='Единица измерения',
        help_text='Единица измерения для фильтра'
    )

    def __str__(self):
        return f'Категория - "{self.category.name}" | Характеристика -"{self.feature_name}"'
    

class ProductFeatureValidators(models.Model):
    category = models.ForeignKey(Category,verbose_name='Категория',on_delete=models.CASCADE)
    feature= models.ForeignKey(ProductFeatures, verbose_name='Характеристика',null=True,blank=True,on_delete=models.CASCADE)
    feature_value= models.CharField(max_length=255,unique=True,null=True,blank=True,verbose_name='Значение хар-ки')

    def __str__(self):
        if not self.feature:
            return f'Валидатор категории "{self.category.name}"- Хар-ка не выбрана'
        return f'Валидатор категории"{self.category.name} | '\
                f'Характеристика - "{self.feature.feature_name}"|'\
                f'Значение - "{self.feature_value}"'


class CartProduct(models.Model):

    class Meta:
        verbose_name = 'Продукт для корзины'
        verbose_name_plural = 'Продукты для корзины'

    user  = models.ForeignKey('Customer',verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart',verbose_name='Корзина',on_delete=models.CASCADE,related_name='related_products')
    # #########################################&&&&&&&&&&?????????????????????????????
    product= models.ForeignKey(Product,verbose_name='Товар',on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Общая сумма')
    
    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.product.price
        super().save(*args, **kwargs)


class Cart(models.Model):

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    owner = models.ForeignKey('Customer',null=True, verbose_name='Владелец',on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct,blank=True,related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=10,default=0, decimal_places=2,verbose_name='Общая сумма')
    in_order= models.BooleanField(default=False)
    for_anonymoys_user= models.BooleanField(default=False)
        
    def __str__(self):
        return str(self.id)

    # def save(self,*args,**kwargs):
    #     cart_data= self.products.aggregate(models.Sum('final_price'),models.Count('id'))
    #     if cart_data.get('final_price__sum'):
    #         self.final_price = cart_data.get('final_price__sum')
    #     else:
    #         self.final_price=0
    #     self.total_products = cart_data['id__count']

# cart.related_producr.all() продукты в корзине
class Customer(models.Model):

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    adress = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Order(models.Model):

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    STATUS_NEW ='new'
    STATUS_IN_PROGRESS='in_progress'
    STATUS_READY= 'is_ready'
    STATUS_COMPLETED= 'completed'
    STATUS_DEACTIVE='deactive'

    BUYING_TYPE_SELF= 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES= (
        (STATUS_NEW,'Новый заказ'),
        (STATUS_IN_PROGRESS,'Заказ в обработке'),
        (STATUS_READY,'Заказ готов'),
        (STATUS_COMPLETED,'Заказ выполнен'),
        (STATUS_DEACTIVE,'Заказ Отменен')
    )

    BUYING_TYPE_CHOICES=(
        (BUYING_TYPE_SELF,'Самовывоз'),
        (BUYING_TYPE_DELIVERY,'Доставка')
        )


    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
    adress = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    otdel = models.CharField(max_length=20,verbose_name='Отделение', null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказ',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Тип заказа',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str(self.id)






# class Specification(models.Model):
#     contet_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     name = models.CharField(max_length=250,verbose_name="Имя товара для характеристик")

#     def __str__(self):
#         return "Характеристики для товара: {}".format(self.name)
