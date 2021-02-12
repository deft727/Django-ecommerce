from django.db import models


# лайки(пост,кол-во лайков), категории(титл,слаг), теги , 
# посты(титл.слаг.контент.дата.картинка,кол-во просмотров,категрия,теги)


class Category(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название категории')
    slug = models.SlugField(max_length=220,verbose_name='Url категории',unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категории'
        ordering = ['title']

class Tag(models.Model):
    title = models.CharField(max_length=55,verbose_name='Название тега')
    slug = models.SlugField(max_length=220,verbose_name='Url слага',unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название статьи')
    slug = models.SlugField(max_length=220,verbose_name='Url статьи',unique=True)
    author = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True,verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='blog/photos/%Y/%m/%d/',blank=True)
    views = models.IntegerField (default=0,verbose_name='Кол-во просотров')
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='posts')
    tags = models.ManyToManyField(Tag,blank=True,related_name='posts')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Посты'
        ordering = ['-created_at']