from .models import Category,TopText
from django.template import context_processors

def single_well_info(request):
    category = Category.objects.all()
    toptext=TopText.objects.all()
    # session_id = request.session._get_or_create_session_key()
    
    if not request.session.session_key:
        request.session.create()


    return {
        'topcategory': category,
        'toptext':toptext,
    }
