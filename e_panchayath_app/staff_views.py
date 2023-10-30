from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.views.generic import TemplateView
from e_panchayath_app.models import Citizen, Product


class Indexview(TemplateView):
    template_name = 'staff/index.html'
    
class Addproduct(TemplateView):
    template_name = 'staff/addproduct.html'   
    def post(self, request,*args,**kwargs):
        # user = User.objects.get(pk=self.request.user.id)
        name = request.POST['name']
        price = request.POST['price']
        desc = request.POST['desc']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)
        se = Product()
        # se.user=user
        se.name = name
        se.image=filesss
        se.price = price
        se.desc = desc
        se.save()
        return redirect(request.META['HTTP_REFERER'], {'message': "product successfully added "})

class View_Product(TemplateView):
    template_name = 'staff/productview.html'
    def get_context_data(self, **kwargs):
        context = super(View_Product, self).get_context_data(**kwargs)
        view_pp = Product.objects.all()
        context['view_pp'] = view_pp
        return context
    
class Reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        Product.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])