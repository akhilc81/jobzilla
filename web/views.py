from django.shortcuts import render,redirect
from .models import Contact,Post_job
from .form import Post_jobForm
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context={ }
    return render(request,"web/index.html",context)

def job_lists(request):
    context={ }
    return render(request,"web/job-list.html",context)

@login_required()
def dash_post_job(request):
    context={ }
    
    # if request.method=="POST":
    #     form=Post_jobForm(deta=request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         obj=form.instance
    #         return render('web:index',{ "obj":obj})
        
    # else:
    #     form=Post_jobForm()
    #     post_job=Post_job.objects.all()
    #     return redirect("web:dash_post_job",{"post_job":post_job,"form":form})    
    
    return render(request,"web/dash-post-job.html",context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, number=number, subject=subject, message=message)
        print(name,email)
        contact.save()
        return redirect('web:contact')
    
    return render(request, 'web/contact.html')




def employer_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        # user = User.objects.filter(username=username,password=password).first()
        if user is not None:
            login(request,user)
            return redirect('web:index')
        else:  
            print('hi')
            return redirect('web:employer_login')
    return render(request,"web/employer_login.html")
    # return render(request,'web/employer_login.html',context)

def employer_register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:employer_login')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:employer_login')
            else:
                customer = User.objects.create_user(username=username,email=email,password=pass1)
                return redirect('web:employer_login')
           

    return render(request,"web/employer_register.html")


# def candidate_register(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')
#         if(pass1!=pass2):
#             print('password not equal'*20)
#             return redirect('web:candidate_register')
#         else:
#             if User.objects.filter(username=username).exists():
#                 print('user already exist')
#                 return redirect('web:candidate_register')
#             else:
#                 customer = User.objects.create_user(username=username,email=email,password=pass1)
#                 return redirect('web:candidate_login')
           

#     return render(request,"web/candidate_register.html")



# def candidate_login(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user =authenticate(request,username=username, password=password)
#         # user = User.objects.filter(username=username,password=password).first()
#         if user is not None:
#             login(request,user)
#             return redirect('web:index')
#         else:  
#             print('hi')
#             return redirect('web:candidate_login')
#     return render(request,"web/candidate-login.html")
#     # return render(request,'web/employer_login.html',context)



# def candidate_signup(request):
    
    
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         firstname =request.POST.get('firstname')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')
        
#         candidate = User.objects.create_user(username,email,pass1)
#         candidate.firstname=firstname
#         candidate.save()
        
#         return redirect('web:candidate_login')
        
    
#     return render(request,'web/candidate-signup.html')




def candidate_logout(request):
    logout(request)
    return redirect('web:index')

def candidate_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        # user = User.objects.filter(username=username,password=password).first()
        if user is not None:
            login(request,user)
            return redirect('web:index')
        else:  
            print('hi')
            return redirect('web:candidate_login')
    return render(request,"web/candidate_login.html")
    

def candidate_register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:employer_register')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:candidate_register')
            else:
                customer = User.objects.create_user(username=username,email=email,password=pass1)
                return redirect('web:candidate_login')
           

    return render(request,"web/candidate_register.html")


