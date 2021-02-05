import sys
from PIL import Image
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
# from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from mptt.models import MPTTModel, TreeForeignKey,TreeManyToManyField
from django.contrib.sessions.models import Session

# from eav.decorators import register_eav


User=get_user_model()


class Category(MPTTModel):

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,on_delete=models.PROTECT)
    name = models.CharField(max_length=250,verbose_name='Имя категории')
    slug = models.SlugField(unique=True)
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):



        try:

            ancestors = self.get_ancestors(include_self=True)
            ancestors = [i.name for i in ancestors]
        except:
            ancestors = [self.name]

        return ' > '.join(ancestors[:len(ancestors) + 1])

    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug': self.slug})

    def get_products(self):
            return self.category.all()

    # @property
    # def get_products(self):
    #      return Product.objects.filter(category=self.children)
 
    # def get_fields_for_filter_in_template(self):
    #     return ProductFeatures.objects.filter(
    #         category=self,
    #         use_in_filter=True
    #     ).prefetch_related('category').value('feature_key','feature_measure','feature_name','filter_type')
    # @property
    # def get_products(self):
    #     return Product.objects.filter(category__name=self.name)

class Size(models.Model):
    
    class Meta:
        verbose_name = 'Размеры'
        verbose_name_plural = 'Размеры'

    foot_size = models.CharField(max_length=50)
    # gender = models.CharField(max_length=50,choices=(('F', 'Female'), ('M', 'Male'), ('U', 'Ungendered')))
    
    def __str__(self):
        return self.foot_size


class Product(models.Model):

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        order_with_respect_to='slug'

    category =  TreeForeignKey(Category, blank=True, null=True, related_name='category', verbose_name="Выберите категорию",on_delete=models.PROTECT)
    title = models.CharField(max_length=250,verbose_name='Наименоватние продукта')
    slug=models.SlugField(unique=True)
    image1 = models.ImageField(verbose_name='Главное изображение',upload_to='images/photos/%Y/%m/%d/')
    image2 = models.ImageField(null=True,blank=True, verbose_name='Изображение 2',upload_to='images/products/%Y/%m/%d/')
    image3 = models.ImageField(null=True,blank=True, verbose_name='Изображение 3',upload_to='images/products/%Y/%m/%d/')
    image4 = models.ImageField(null=True,blank=True, verbose_name='Изображение 4',upload_to='images/products/%Y/%m/%d/')
    image5 = models.ImageField(null=True,blank=True, verbose_name='Изображение 5',upload_to='images/products/%Y/%m/%d/')
    features = models.ManyToManyField("specs.ProductFeatures", blank=True, related_name='features_for_product')
    sizes = models.ManyToManyField(Size,verbose_name='размеры', help_text="Выберите доступные размеры продукта")
    available = models.BooleanField(default=True,verbose_name="Наличие")
    description = models.TextField(verbose_name='Описание товара',null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена')
    old_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Старая Цена',null=True,blank=True)

    def __str__(self):
        return self.title

    def get_products(self):
        return self.children.all()

    def get_model_name(self):
        return self.__class__.__name__.lower()

    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'slug':self.slug})

    def get_features(self):
        return {f.feature.feature_name: ' '.join([f.value, f.feature.unit or ""]) for f in self.features.all()}

    # def get_feature_value_by_key(self,key):
        # return self.characteristics.get(key)


    def save(self,*args,**kwargs):

        image1=self.image1
        if image1 :

            img1=Image.open(image1)
            new_img1=img1.convert('RGB')
            res_img1=new_img1.resize((800,800),Image.ANTIALIAS)
            filestream= BytesIO()
            file_=res_img1.save(filestream,'JPEG',quality=90)
            filestream.seek(0)
            name= '{}.{}'.format(*self.image1.name.split('.'))
            self.image1 = InMemoryUploadedFile(
                filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
            )
            super().save(*args,**kwargs)
        
        image2=self.image2
        if image2 :

            img2=Image.open(image2)
            new_img2=img2.convert('RGB')
            res_img2=new_img2.resize((800,800),Image.ANTIALIAS)
            filestream= BytesIO()
            file_=res_img2.save(filestream,'JPEG',quality=90)
            filestream.seek(0)
            name= '{}.{}'.format(*self.image2.name.split('.'))
            self.image2 = InMemoryUploadedFile(
                filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
            )
            super().save(*args,**kwargs)

        image3=self.image3
        if image3 :

            img3=Image.open(image3)
            new_img3=img3.convert('RGB')
            res_img3=new_img3.resize((800,800),Image.ANTIALIAS)
            filestream= BytesIO()
            file_=res_img3.save(filestream,'JPEG',quality=90)
            filestream.seek(0)
            name= '{}.{}'.format(*self.image3.name.split('.'))
            self.image3 = InMemoryUploadedFile(
                filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
            )
            super().save(*args,**kwargs)

        image4=self.image4
        if image4 :

            img4=Image.open(image4)
            new_img4=img4.convert('RGB')
            res_img4=new_img4.resize((800,800),Image.ANTIALIAS)
            filestream= BytesIO()
            file_=res_img4.save(filestream,'JPEG',quality=90)
            filestream.seek(0)
            name= '{}.{}'.format(*self.image4.name.split('.'))
            self.image4 = InMemoryUploadedFile(
                filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
            )
            super().save(*args,**kwargs)

        
        image5=self.image5
        if image5 :

            img5=Image.open(image5)
            new_img5=img5.convert('RGB')
            res_img5=new_img5.resize((800,800),Image.ANTIALIAS)
            filestream= BytesIO()
            file_=res_img5.save(filestream,'JPEG',quality=90)
            filestream.seek(0)
            name= '{}.{}'.format(*self.image5.name.split('.'))
            self.image5 = InMemoryUploadedFile(
                filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
            )
            super().save(*args,**kwargs)

    # @classmethod
    # def get_products_brands(cls,category):
    #     return list(filter(
    #         lambda x: x is not None,
    #         [p.characteristics.get('brand') for p in cls.objects.filter(category=category)]
    #     ))

class TopText(models.Model):
    class Meta:
        verbose_name='текст в бегущей строке'
    title=models.CharField(max_length=50,verbose_name='Заголовок',null=True,blank=True)
    text= models.CharField(max_length=250,verbose_name='текст в бегущей строке',null=True,blank=True)
    
    def __str__(self):
            return self.title


class MyTopImage(models.Model):
    class Meta:
        verbose_name='Изображение сверху'
        verbose_name_plural = 'Изображения сверху'
    image1=models.ImageField(null=True,blank=True, verbose_name='Изображение 1',upload_to='images/TopImage/')
    image2=models.ImageField(null=True,blank=True, verbose_name='Изображение 2',upload_to='images/TopImage/')

    # def __str__(self):
    #     return self.verbose_name
    # def save(self,*args,**kwargs):

    #     image1=self.image1
    #     if image1 :

    #         img1=Image.open(image1)
    #         new_img1=img1.convert('RGB')
    #         res_img1=new_img1.resize((1920,650),Image.ANTIALIAS)
    #         filestream= BytesIO()
    #         file_=res_img1.save(filestream,'JPEG',quality=90)
    #         filestream.seek(0)
    #         name= '{}.{}'.format(*self.image1.name.split('.'))
    #         self.image1 = InMemoryUploadedFile(
    #             filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
    #         )
    #         super().save(*args,**kwargs)
        
    #     image2=self.image2
    #     if image2 :

    #         img2=Image.open(image2)
    #         new_img2=img2.convert('RGB')
    #         res_img2=new_img2.resize((1920,650),Image.ANTIALIAS)
    #         filestream= BytesIO()
    #         file_=res_img2.save(filestream,'JPEG',quality=90)
    #         filestream.seek(0)
    #         name= '{}.{}'.format(*self.image2.name.split('.'))
    #         self.image2 = InMemoryUploadedFile(
    #             filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
    #         )
    #         super().save(*args,**kwargs)

class MyImage(models.Model):
    class Meta:
        verbose_name='Изображение снизу'
        verbose_name_plural = 'Изображения снизу'
    imagedown1=models.ImageField(null=True,blank=True, verbose_name='Изображение 1',upload_to='images/DownImage')
    imagedown2= models.ImageField(null=True,blank=True, verbose_name='Изображение 2',upload_to='images/DownImage')

    def save(self,*args,**kwargs):
        imagedown1=self.imagedown1
        img=Image.open(imagedown1)
        new_img=img.convert('RGB')
        res_img=new_img.resize((958,401),Image.ANTIALIAS)
        filestream= BytesIO()
        file_=res_img.save(filestream,'JPEG',quality=90)
        filestream.seek(0)
        name= '{}.{}'.format(*self.imagedown1.name.split('.'))
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
        name= '{}.{}'.format(*self.imagedown2.name.split('.'))
        self.imagedown2 = InMemoryUploadedFile(
            filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
        )
        super().save(*args,**kwargs)

class ChangeMyInfo(models.Model):
    class Meta:
        verbose_name='Изменить адрес'
        verbose_name_plural = 'Изменить адреса'
    toptext = models.CharField(max_length=150,verbose_name='Текст в левом углу',null=True,blank=True)
    adress1= models.CharField(max_length=150,verbose_name='Адресс 1',null=True,blank=True)
    street1= models.CharField(max_length=150,verbose_name='Улица для адресс 1',null=True,blank=True)
    email1= models.EmailField(max_length=150,verbose_name='емайл для адрес 1',null=True,blank=True)
    phone1= models.CharField(max_length=20, verbose_name='Номер телефона')
    adress2 = models.CharField(max_length=150,verbose_name='Адресс 2',null=True,blank=True)
    street2=  models.CharField(max_length=150,verbose_name='Улица для адресс 2',null=True,blank=True)
    email2= models.EmailField(max_length=150,verbose_name='Емайл для адрес 2',null=True,blank=True)
    phone2= models.CharField(max_length=20, verbose_name='Номер телефона')
    about=  models.CharField(max_length=150,verbose_name='Пару слов о сайте',null=True,blank=True)
    def __str__(self):
        return 'Изменение информации'

class Logo(models.Model):
    class Meta:
        verbose_name='логотип и  соц.сети'
        verbose_name_plural = 'логотип и  соц.сети'

    logo=models.ImageField(null=True,blank=True, verbose_name='Логотип',upload_to='images/Logo')
    insta = models.URLField(null=True,blank=True, verbose_name='Инстаграмм')
    twiter = models.URLField(null=True,blank=True, verbose_name='Твитер')
    facebook = models.URLField(null=True,blank=True, verbose_name='Фейсбук')
    
    def save(self,*args,**kwargs):
        imagedown2=self.logo
        img=Image.open(imagedown2)
        new_img=img.convert('RGB')
        res_img=new_img.resize((362,129),Image.ANTIALIAS)
        filestream= BytesIO()
        file_=res_img.save(filestream,'JPEG',quality=90)
        filestream.seek(0)
        name= '{}.{}'.format(*self.logo.name.split('.'))
        self.logo = InMemoryUploadedFile(
            filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
        )
        super().save(*args,**kwargs)

class AboutUs(models.Model):
    class Meta:
        verbose_name='Информация на странице о Нас'
        verbose_name_plural = 'Информация на странице о Нас'

    title = models.CharField(max_length=150, verbose_name='Заголовок',null=True,blank=True)
    text = models.TextField(max_length=1500, verbose_name='Текст',null=True,blank=True)
    img= models.ImageField(null=True,blank=True, verbose_name='Изображение ',upload_to='images/AboutImage/')
    def __str__(self):
        return self.title


class Returns(models.Model):
    class Meta:
        verbose_name='Информация на странице о Возврате'
        verbose_name_plural = 'Информация на странице о Возврате'

    returns = models.CharField(max_length=250,verbose_name='Заголовок',null=True,blank=True)
    returnsText = models.CharField(max_length=700,verbose_name='Дополнительный Текст',null=True,blank=True)
    def __str__(self):
        return self.returns


class Delivery(models.Model):

    class Meta:
        verbose_name='Информация на странице о Доставке'
        verbose_name_plural = 'Информация на странице о Доставке'

    title = models.CharField(max_length=150,verbose_name='Заголовок',null=True,blank=True)
    text = models.TextField(max_length=1500,verbose_name='Текст',null=True,blank=True)

    def __str__(self):
        return self.title



class ReturnsItem(models.Model):

    class Meta:
        verbose_name='Информация на странице о Возврате'
        verbose_name_plural = 'Информация на странице о Возврате'

    title = models.CharField(max_length=150,verbose_name='Заголовок',null=True,blank=True)
    text = models.TextField(max_length=1500,verbose_name='Текст',null=True,blank=True)

    def __str__(self):
        return self.title



class ContactUs(models.Model):

    class Meta:
        verbose_name='Информация на странице Контактов'
        verbose_name_plural = 'Информация на странице Контактов'
    title = models.CharField(max_length=150,verbose_name='Заголовок',null=True,blank=True)
    text = models.TextField(max_length=150,verbose_name='Текст',null=True,blank=True)
    phone = models.CharField(max_length=25,verbose_name="Телефон",null=True,blank=True)
    instatitle = models.CharField(max_length=100,verbose_name=" Название страницы Инстаграмм",null=True,blank=True)
    insta = models.CharField(max_length=100,verbose_name="адресс Инстаграмм",null=True,blank=True)
    facebooktitle = models.CharField(max_length=100,verbose_name=" Название страницы Фейсбук",null=True,blank=True)
    facebook = models.CharField(max_length=100,verbose_name="адресс Фейсбук",null=True,blank=True)
    def __str__(self):
        return self.title

# class ProductFeatureValidators(models.Model):
    # category = models.ForeignKey(Category,verbose_name='Категория',on_delete=models.CASCADE)
    # feature= models.ForeignKey(ProductFeatures, verbose_name='Характеристика',null=True,blank=True,on_delete=models.CASCADE)
    # feature_value= models.CharField(max_length=255,unique=True,null=True,blank=True,verbose_name='Значение хар-ки')

    # def __str__(self):
    #     if not self.feature:
    #         return f'Валидатор категории "{self.category.name}"- Хар-ка не выбрана'
    #     return f'Валидатор категории"{self.category.name} | '\
    #             f'Характеристика - "{self.feature.feature_name}"|'\
    #             f'Значение - "{self.feature_value}"'


class CartProduct(models.Model):

    class Meta:
        verbose_name = 'Продукт для корзины'
        verbose_name_plural = 'Продукты для корзины'
    user  = models.ForeignKey('Customer',verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart',verbose_name='Корзина',on_delete=models.CASCADE,related_name='related_products')
    product= models.ForeignKey(Product,verbose_name='Товар',on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=150,verbose_name='Размер',null=True,blank=True)
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



class Whishlist(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product,blank=True,related_name='Продукты',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.owner)


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
        (BUYING_TYPE_SELF,'Отделение'),
        (BUYING_TYPE_DELIVERY,'Курьер')
        )

    PAY_TYPE_NAL = 'nal'
    PAY_TYPE_PAY = 'pay'
    PAY_TYPE_NOT_PAY = 'not_pay'
    PAY_TYPE_MISS= 'miss'
    PAY_TYPE_WAIT= 'wait'


    PAY_TYPE_CHOICES=(
        (PAY_TYPE_PAY,'Олачен'),
        (PAY_TYPE_NOT_PAY,'Отклонен'),
        (PAY_TYPE_MISS,'Ошибка при оплате'),
        (PAY_TYPE_NAL,'Наложенный платеж'),
        (PAY_TYPE_WAIT,'Ожидание платежа'),
        )


    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон',help_text="+38-050-111-11-11")
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
    email= models.EmailField(max_length=60, verbose_name='Емайл', null=True, blank=True)
    adress = models.CharField(max_length=60, verbose_name='Город', null=True, blank=True)
    otdel = models.CharField(max_length=20,verbose_name='Отделение', null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказа',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Доставка',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    status_pay =  models.CharField(
        max_length=100,
        verbose_name='Оплата',
        choices=PAY_TYPE_CHOICES,
        default=PAY_TYPE_NAL
    )

    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    pay = models.CharField(max_length=100,verbose_name='Cпособ оплаты' , null=True,blank=True)

    def __str__(self):
        return "Заказ: {} {} {}".format(self.id, self.first_name, self.last_name)

class Rewiews(models.Model):

    name= models.CharField(max_length=255, verbose_name='Имя')
    text= models.TextField('Сообщение',max_length=500)
    parent= models.ForeignKey(
        'self',verbose_name='Родитель',on_delete=models.SET_NULL,blank=True,null=True
    )
    product=models.ForeignKey(Product,verbose_name='Продукт',on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True,db_index=True,verbose_name='Добавлено')

    def __str__(self):
        return f"{self.name}-{self.product}"

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'



