from .models import Category
from django.template import context_processors

def single_well_info(request):
    category = Category.objects.all()
       
    # session_id = request.session._get_or_create_session_key()
    
    if not request.session.session_key:
        request.session.create()


    return {
        'topcategory': category,
    }
