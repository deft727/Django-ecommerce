from .models import Product,Category,TopText,ChangeMyInfo,Logo
from django.db.models import Q
from django.template import context_processors
from django.core.paginator import Paginator
from specs.models import ProductFeatures,CategoryFeature

from django.core.mail import send_mail

def single_well_info(request):
    category = Category.objects.all().prefetch_related('parent')
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
