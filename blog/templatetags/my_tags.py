from django import template
from blog.models import Tag,Category,Post
from mainapp.models import Product
from django.db.models import Count,F


register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.annotate(cnt=Count('posts',filter=F('posts__is_publish'))).filter(cnt__gt=0)

@register.simple_tag()
def get_tags():
    return Tag.objects.all()

@register.simple_tag()
def get_new_posts():
    return Post.objects.order_by('-created_at')[:3]

@register.simple_tag()
def get_popular_products():
    return Product.objects.order_by('?')[:3]