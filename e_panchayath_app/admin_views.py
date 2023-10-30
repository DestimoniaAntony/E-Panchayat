from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from e_panchayath_app.models import Application, Citizen, Service, Staff

class Indexview(TemplateView):
    template_name = 'admin/index.html'
    
class Citizen_tableview(TemplateView):
    template_name = 'admin/citizen_table.html'
    
    def get_context_data(self, **kwargs):
        context = super(Citizen_tableview,self).get_context_data(**kwargs)

        citizen = Citizen.objects.all()
        #user=service_provider.objects.all()
        context['citizen'] = citizen
        return context

class Staff_tableview(TemplateView):
    template_name = 'admin/staff_table.html'
    
    def get_context_data(self, **kwargs):
        context = super(Staff_tableview,self).get_context_data(**kwargs)

        staff = Staff.objects.all()
        #user=service_provider.objects.all()
        context['staff'] = staff
        return context
    
class AddServiceView(TemplateView):
    template_name = 'admin/create_service.html'   

    def post(self, request, *args, **kwargs):

        name = request.POST['service']
        fe = Service()

        fe.service= name
        fe.save()
        return render(request, 'admin/index.html', {'message': "Successfully added"})
    
class AppliedServicesview(TemplateView):
    template_name = 'admin/appliedservice.html'

    def get_context_data(self, **kwargs):
        context = super(AppliedServicesview, self).get_context_data(**kwargs)

        app = Application.objects.filter(status='applied')
        context['app'] = app

        return context
    

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        accept = Application.objects.get(pk=id)
        accept.status = 'Approve'
        accept.save()
        return render(request, 'admin/index.html', {'message': "Approve"})
    

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        reject = Application.objects.get(pk=id)
        reject.status = 'Approve'
        reject.save()
        return render(request, 'admin/index.html', {'message': "Reject"})
