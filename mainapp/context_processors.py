from .models import Product,Category,TopText,ChangeMyInfo,Logo
from django.db.models import Q
from django.template import context_processors
from django.core.paginator import Paginator
from specs.models import ProductFeatures,CategoryFeature

from django.views.decorators.cache import cache_page
from django.core.cache import cache

from django.core.mail import send_mail



def single_well_info(request):
    categories = cache.get('categories')
    if not categories:
        category = Category.objects.all().prefetch_related('parent')
        cache.set('categories',categories,600)
    toptext=TopText.objects.all()
    myinfo= ChangeMyInfo.objects.all()
    logo = Logo.objects.all()
      
    if not request.session.session_key:


        x = ' Ктото зашел на сайт '
        send_mail('Welcome!',x, "Yasoob",['zarj09@gmail.com'], fail_silently=False)


        request.session.create()

    return {
        'topcategory': category,
        'toptext':toptext,
        'myinfo': myinfo,
        'logo': logo,
    }
