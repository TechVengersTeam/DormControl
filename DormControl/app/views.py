from django.shortcuts import render
# from .forms import StudentInfoForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from .models import GatePass

# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    # return render(request, "register.html")
    return render(request, "home.html")

# def register(request):
#     if request.method == 'POST':
#         form = StudentInfoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username = username, password = password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = StudentInfoForm(request.POST)
#     return render(request, 'home.html', {'form': form})

def register(request):
    if request.method == "POST":
        libid = request.POST['libid']
        email = request.POST['email']
        name = request.POST['name']
        course = request.POST['course']
        branch = request.POST['branch']
        year = request.POST['year']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']

        myuser = User.objects.create_user(username= email, email=email, password=password)
        myuser.first_name = name
        # myuser.name = name
        # myuser.course = course
        # myuser.branch = branch
        # myuser.year = year
        # myuser.phone = phone
        # myuser.address = address
        myuser.save()
        print(myuser)
        print("Done")
        # user = authenticate()
        return redirect('home')
    else:
        return render(request, 'register.html')
    
# def adminLogin(request):
#     return render(request, 'adminLogin.html')

def studentLogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def adminLogin(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('/')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_staff == True:
            login(request, user)
            return redirect('/adminfront')
        else:
            return redirect('/adminLogin')
    else:
        return render(request, 'adminLogin.html')
    

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect("/")
    else:
        return render(request, 'dashboard.html')
    
@login_required
def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'fashion.pdf'
    # Define the full file path
    filepath = BASE_DIR + '/static/pdf/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

def mess(request):
    return render(request, 'mess.html')

@login_required
def adminfront(request):
    if request.user.is_staff:
        return render(request, 'adminfront.html')
    else:
        return redirect("/")

@login_required
def complaints(request):
    return render(request, "complaints.html")

@login_required
def checkInOut(request):
    return render(request, "check-in-out.html")

@login_required
def gatepassdetails(request):
    if request.user.is_staff:
        all_pass= GatePass.objects.all()
    
        context= {'allpass': all_pass}
        return render(request, 'gatepassdetails.html', context=context)
    else:
        return redirect("/")


@login_required
def complaintsdetails(request):
    if request.user.is_staff:
        return render(request, 'complaintsdetails.html')
    else:
        return redirect("/")


@login_required
def studentdetails(request):
    if request.user.is_staff:
        all_users= get_user_model().objects.all()
    
        context= {'allusers': all_users}
        
        return render(request, 'studentdetails.html', context)
    else:
        return redirect("/")
