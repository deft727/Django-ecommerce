from .models import Product,Category,TopText,ChangeMyInfo,Logo
from django.db.models import Q
from django.template import context_processors
from django.core.paginator import Paginator



def single_well_info(request):
    category = Category.objects.all()
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

# class MyQ(Q):
#     default = 'OR'

    
# class SearchResultsView(ListView):
#     model = Category
#     template_name = 'category_detail.html'
#     slug_url_kwarg = 'slug'
#     def get_context_data(self,*args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         query = self.request.GET.get('search')
#         page_number = self.request.GET.get('page',1)
#         if query:
#             if query[0].lower():
#                 query= query.title()
#             products =   Product.objects.filter(Q(title__icontains=query))
            
#             paginator = Paginator(products, 19)  # 3 поста на каждой странице  
#             page =paginator.get_page(page_number) 
#             context['category_products'] =page
#             context['page']= page

#             return context