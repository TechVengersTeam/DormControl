from django.shortcuts import render
# from .forms import StudentInfoForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout



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
            return redirect('/')
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
            return redirect('/')
        else:
            return redirect('/adminLogin')
    else:
        return render(request, 'adminLogin.html')
    
# def signin(request):
#     if request.user.is_authenticated:
#         return render(request, 'homepage.html')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         else:
#             form = AuthenticationForm(request.POST)
#             return render(request, 'signin.html', {'form': form})
#     else:
#         form = AuthenticationForm()
#         return render(request, 'signin.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')