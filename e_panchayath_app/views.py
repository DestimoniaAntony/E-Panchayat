from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from e_panchayath_app.models import Citizen, Staff, UserType
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
 
class loginview(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "users":
                    return redirect('/users')
                elif UserType.objects.get(user_id=user.id).type == "staff":
                    return redirect('/staff')
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})
        
class User_RegView(TemplateView):
    template_name = 'user_reg.html'   

    def post(self, request, *args, **kwargs):
        first_name = request.POST['fname']
        email = request.POST['mail']
        mobile = request.POST['number']
        gender = request.POST['gender']
        marital = request.POST['marital']
        dob = request.POST['date']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        pincode = request.POST['pincode']
        panchayat = request.POST['panchayat']
        ward = request.POST['number']
        password = request.POST['password']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'user_reg.html', {'message': "already added the username or email"})

        else:
            user = User.objects.create_user(username=email, password=password, first_name=first_name, email=email,
                                            is_staff='0', last_name='1')
            user.save()
            reg = Citizen()
            reg.user = user
            reg.mobile = mobile
            reg.gender = gender
            reg.marital_status = marital
            reg.birth_date = dob
            reg.address_line1 = address1
            reg.address_line2 = address2
            reg.pincode = pincode
            reg.panchayat = panchayat
            reg.ward = ward
            reg.password = password
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "users"
            usertype.save()
            # messages="Registered Successfully"

            return render(request, 'index.html', {'message': "successfully added"})

class Staff_RegView(TemplateView):
    template_name = 'staff_reg.html'   

    def post(self, request, *args, **kwargs):
        first_name = request.POST['fname']
        email = request.POST['mail']
        mobile = request.POST['number']
        gender = request.POST['gender']
        marital = request.POST['marital']
        dob = request.POST['date']
        qualification = request.POST['qualification']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        pincode = request.POST['pincode']
        password = request.POST['password']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'user_reg.html', {'message': "already added the username or email"})

        else:
            user = User.objects.create_user(username=email, password=password, first_name=first_name, email=email,
                                            is_staff='0', last_name='1')
            user.save()
            reg = Staff()
            reg.user = user
            reg.mobile = mobile
            reg.gender = gender
            reg.marital_status = marital
            reg.birth_date = dob
            reg.address_line1 = address1
            reg.address_line2 = address2
            reg.pincode = pincode
            reg.qualification = qualification
            reg.password = password
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "staff"
            usertype.save()
            # messages="Registered Successfully"

            return render(request, 'index.html', {'message': "successfully added"})

