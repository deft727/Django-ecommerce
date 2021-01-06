from .models import Category,TopText,ChangeMyInfo
# from .mixins import CartMixin
from django.template import context_processors

def single_well_info(request):
    # cart=CartMixin()
    category = Category.objects.all()
    toptext=TopText.objects.all()
    myinfo= ChangeMyInfo.objects.all()
    if not request.session.session_key:
        request.session.create()


    return {
        'topcategory': category,
        'toptext':toptext,
        'myinfo': myinfo,
    }


