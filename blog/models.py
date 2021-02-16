from django.db import models
from django.urls import reverse
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# лайки(пост,кол-во лайков), категории(титл,слаг), теги , 
# посты(титл.слаг.контент.дата.картинка,кол-во просмотров,категрия,теги)


class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название категории')
    slug = models.SlugField(max_length=220,verbose_name='Url категории',unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('category',kwargs={"slug":self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=55,verbose_name='Название тега')
    slug = models.SlugField(max_length=220,verbose_name='Url слага',unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('tag',kwargs={"slug":self.slug})

class Post(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название статьи')
    slug = models.SlugField(max_length=220,verbose_name='slug статьи',unique=True)
    author = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True,verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='blog/photos/%Y/%m/%d/',blank=True)
    views = models.IntegerField (default=0,verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='posts')
    tags = models.ManyToManyField(Tag,blank=True,related_name='posts')
    url = models.URLField(null=True,blank=True,verbose_name='Ссылка на товар (если есть)')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={"slug":self.slug})


    # def save(self,*args,**kwargs):

    #     photo=self.photo
    #     if photo :

    #         img1=Image.open(photo)
    #         new_img1=img1.convert('RGB')
    #         res_img1=new_img1.resize((810,450),Image.ANTIALIAS)
    #         filestream= BytesIO()
    #         file_=res_img1.save(filestream,'JPEG',quality=90)
    #         filestream.seek(0)
    #         name= '{}.{}'.format(*self.photo.name.split('.'))
    #         self.photo = InMemoryUploadedFile(
    #             filestream,'ImageFiedl',name,'jpeg/image',sys.getsizeof(filestream),  None
    #         )
    #         super().save(*args,**kwargs)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']