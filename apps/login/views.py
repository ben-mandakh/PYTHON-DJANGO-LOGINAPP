################### IMPORT SECTION ########################
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

#################### INDEX PAGE ###########################
def index(request):                
    return render(request, "login/index.html")

def process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        newUser=User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password = hashed_password)
        newUser.save()
        request.session['id']=newUser.id
        messages.success(request, "User successfully registered")
        return redirect("/success")

################### REGISTRATION FUNCTION #################

def success(request):                
    context = {"user": User.objects.get(id = request.session['id'])}
    return render(request, "login/show.html", context)

################### LOGIN FUNCTION HERE ###################

def login(request):
    if (User.objects.filter(email=request.POST['email']).exists()):
        user = User.objects.filter(email=request.POST['email'])[0]
        if (bcrypt.checkpw(request.POST['password'].encode(), user.password.encode())):
            request.session['id'] = user.id
            messages.success(request, "User successfully logged in")
            return redirect('/success')
    return redirect('/success')

#################### END  ###################################


































# def show_one(request,id):
#     context = {"show": Show.objects.get(id = id)}
#     return render(request, "show/showOne.html", context)

# def editShow(request, id):                
#     context = {"shows": Show.objects.get(id=id)}
#     return render(request, "show/editShow.html", context)    

# def editShowFunction(request,id):
#     errors = Show.objects.basic_validator(request.POST)
#     if len(errors) > 0:
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect(f'/shows/{id}/edit')
#     else:
#         u = Show.objects.get(id = id)
#         u.title=request.POST['title']
#         u.network=request.POST['network']
#         u.release_date=request.POST['release_date']
#         u.desc = request.POST['desc']
#         u.save()
#         messages.success(request, "Blog successfully updated")
#         return redirect ("/shows")

# def delete(request,id):
#     d = Show.objects.get(id = id)
#     d.delete()
#     return redirect ("/shows")


