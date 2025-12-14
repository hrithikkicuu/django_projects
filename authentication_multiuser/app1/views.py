from django.shortcuts import render,redirect
from django.views import View
from app1.forms import SignupForm



class Home(View):
    def get(self, request):
        return render(request, 'home.html')

class AdminHome(View):
    def get(self, request):
        return render(request, 'adminhome.html')

class StudentHome(View):
    def get(self, request):
        return render(request, 'studenthome.html')

class TeacherHome(View):
    def get(self, request):
        return render(request, 'teacherhome.html')

class Register(View):
    def get(self, request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request, 'register.html', context)

    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('userlogin')
        return render(request,'register.html',{'form':form_instance})



from app1.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

class Userlogin(View):
   def get(self, request):
       form_instance = LoginForm(request.POST)
       context = {'form': form_instance}
       return render(request, 'login.html', context)


   def post(self,request):
       form_instance=LoginForm(request.POST)
       if form_instance.is_valid():
           data=form_instance.cleaned_data #fetch the data after validation
           u=data['username'] #retrieve username from cleaned data
           p=data['password'] #retrieve password from cleaned data
           user=authenticate(username=u,password=p)  #calls authenticate() to verify if user exists
           if user and user.is_superuser==True:
               login(request,user)
               return redirect('adminhome')
           elif user and user.role=='student':
               login(request,user)
               return redirect('studenthome')
           elif user and user.role=='teacher':
               login(request,user)
               return redirect('teacherhome')

           else:#if user does not exist
               messages.error(request,'invalid user credentials')
               return redirect('userlogin')


       # context={'form':form_instance}
       # return render(request,'login.html',context)



class Userlogout(View):
       def get(self, request):
           logout(request) #remove the user from the current section

           return redirect('userlogin')
