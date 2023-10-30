from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from e_panchayath_app.models import Citizen, Product, Request, Service,Application


class Indexview(TemplateView):
    template_name = 'users/index.html'

class Serviceview(TemplateView):
    template_name = 'users/apply_service.html'
    
    def get_context_data(self, **kwargs):
        context = super(Serviceview,self).get_context_data(**kwargs)

        serve = Service.objects.all()
        
        context['serve'] = serve
        return context  

class RequestView(View):
    def dispatch(self,request,*args,**kwargs):
        re = Request.objects.get(user_id=self.request.user.id)

        pid = request.GET['id']
        r=Service.objects.get(pk=pid)
        c = Request()
        c.service_id=pid
        c.save()

        return render(request, 'users/index.html', {'message': "Successfully added"})
    
class UpdateProfile(TemplateView):
    template_name = 'users/update_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        usid = self.request.user.id

        view_cust = Citizen.objects.get(user_id=usid)
        print(view_cust)

        context['view_cust'] = view_cust
        return context
    
    def post(self, request, *args, **kwargs):

        if request.POST['profile'] == "pass":
            id = request.POST['id']
            password = request.POST['password']
            us = User.objects.get(pk=id)

            us.set_password(password)

            us.save()
        else:
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            id = request.POST['id']
            email = request.POST['email']
            number = request.POST['number']
            date = request.POST['date']
            name = request.POST['name']
            pincode = request.POST['pincode']
            panchayat = request.POST['panchayat']
            
            reg = Citizen.objects.get(user=id)

            reg.address1 = address1
            reg.address2 = address2          
            reg.number = number
            reg.date = date           
            reg.pincode = pincode
            reg.panchayat = panchayat
            reg.save()
            us = User.objects.get(pk=id)
            us.username = email
            us.email = email
            us.first_name = name
            us.save()

        messages = "Update Successful."
        return render(request, 'users/index.html', {'messages': "Update Successful"})


class ApplyApplication(TemplateView):
    template_name = 'users/application_form.html' 
    
    def get_context_data(self, **kwargs):
        context = super(ApplyApplication, self).get_context_data(**kwargs)
        service = Service.objects.all()
        context['service'] = service
        return context  

    def post(self, request, *args, **kwargs):
        re = Citizen.objects.get(user_id=self.request.user.id)
        # user = User.objects.get(pk=self.request.user.id)
        image = request.FILES['image']
        ob=FileSystemStorage()
        obj=ob.save(image.name, image)
        service = request.POST['service']
        name = request.POST['fname']
        email = request.POST['mail']
        mobile = request.POST['number']
        qualification = request.POST['qualification']
        gender = request.POST['gender']
        marital = request.POST['marital']
        dob = request.POST['date']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        country = request.POST['country']
        state = request.POST['state']
        district = request.POST['district']
        pincode = request.POST['pincode']
        panchayat = request.POST['panchayat']
        ward = request.POST['ward']
        password = request.POST['password']

       
        reg = Application()
        
        
        reg.image=obj
        reg.service_id=service
        reg.user_id = re.id
        reg.name = name
        reg.email = email
        reg.mobile = mobile
        reg.qualification = qualification
        reg.gender = gender
        reg.marital_status = marital
        reg.birth_date = dob
        reg.address_line1 = address1
        reg.address_line2 = address2
        reg.country = country
        reg.state = state
        reg.district = district  
        reg.pincode = pincode
        reg.panchayat = panchayat
        reg.ward = ward
        reg.password = password
        reg.status='applied'
        reg.save()
        return render(request, 'users/index.html', {'message': "Successfully applied"})
    
class AppliedServicesStatusView(TemplateView):
    template_name = 'users/application_status.html'

    def get_context_data(self, **kwargs):
        context = super(AppliedServicesStatusView, self).get_context_data(**kwargs)
        re = Citizen.objects.get(user_id=self.request.user.id)

        apps = Application.objects.filter(user_id=re.id)
        context['apps'] = apps

        return context
    
class View_Productgallery(TemplateView):
    template_name = 'users/productgallery.html'
    def get_context_data(self, **kwargs):
        context = super(View_Productgallery, self).get_context_data(**kwargs)
        view_pp = Product.objects.all()
        context['view_pp'] = view_pp
        return context