from .models import Product,Category,TopText,ChangeMyInfo,Logo
from django.db.models import Q
from django.template import context_processors
from django.core.paginator import Paginator



def single_well_info(request):
    category = Category.objects.all().prefetch_related('children')
    toptext=TopText.objects.all()
    myinfo= ChangeMyInfo.objects.all()
    logo = Logo.objects.all()
    if not request.session.session_key:
        request.session.create()

    return {
        'topcategory': category,
        'toptext':toptext,
        'myinfo': myinfo,
        'logo': logo,
    }
