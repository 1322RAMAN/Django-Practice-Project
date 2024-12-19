from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .decorators.superuser_decorator import superuser_required
from django.shortcuts import HttpResponse
from .forms import UserRegisterForm, UserLoginForm, ContactForm
from . models import CustomUser


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, "Your account has been created. You can now log in.")
            return redirect('login')  # Replace 'login' with your login URL name
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)  # Use email for authentication
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('home')  # Replace 'home' with your home URL name
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})


def manual_login(request):
    """You can customize the default session-based authentication by manually
        managing user sessions."""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)  # Fetch user by email
            if user.check_password(password):  # Verify the password
                # Manually set session data
                request.session['user_id'] = user.id
                return redirect('home_view')  # Redirect to the home page
            else:
                return render(request, 'user/manual_login.html', {'error': 'Invalid password'})
        except CustomUser.DoesNotExist:
            return render(request, 'user/manual_login.html', {'error': 'User does not exist'})

    # For GET requests, render the login page
    return render(request, 'user/manual_login.html')


def home_view(request):
    """Check for the session on subsequent requests"""
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request, 'user/home.html')


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')  # Replace 'login' with your login URL name


@login_required
def home(request):
    """You can specify the redirect URL if the user is not logged in:
    e.g.(@login_required(login_url='/custom-login/'))"""
    return render(request, 'user/home.html')


@login_required
def get_users(request):
    users = CustomUser.objects.all().values()
    print(users)
    return render(request, 'user/users.html', {'users': users})


@login_required
def get_user(request):
    user = CustomUser.objects.filter(email=request.user.email).first()
    print(user)
    return render(request, 'user/user_detail.html', {'user': user})


@login_required
def make_superuser(request):
    try:
        user = CustomUser.objects.get(email=request.user.email)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return redirect('home')
    except CustomUser.DoesNotExist:
        return redirect('user_details')


def is_superuser(user):
    return user.is_superuser


@user_passes_test(is_superuser)
def my_view(request):
    """You can specify a custom redirect URL if the user fails the test:
    e.g.(@user_passes_test(is_superuser, login_url='/no-access/'))"""
    # view logic here
    return render(request, 'superuser_template.html')


def check_superuser(request):
    superuser = request.user.is_superuser
    if superuser:
        return HttpResponse('<h1>User is Superuser</h1>')
    else:
        return HttpResponse('<h1>User is not Superuser</h1>')


def is_staff_member(request):
    """ The is_staff attribute returns True if the user is marked as a staff member. """
    user = CustomUser.objects.get(email=request.user.email)

    if user.is_staff:
        print("User is a staff member")
        msg = "User is a staff member"
    else:
        print("User is not a staff member")
        msg = "User is not a staff member"
    return HttpResponse(msg)


@login_required
def staff_only_view(request):
    if request.user.is_staff:
        return HttpResponse("Welcome, Staff Member!")
    return HttpResponse("Access Denied")


@staff_member_required
def check_staff_member_required(request):
    """ The @staff_member_required decorator is used to restrict access to views to only staff members. """
    # view logic here
    return HttpResponse("staff_member_required")


@superuser_required
def checking_superuser_decorator(request):
    """ Usage: It restricts access to views to only superusers. """
    # view logic here
    # return render(request, 'superuser_template.html')
    return HttpResponse('superuser_template.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(f"Message from {name} ({email}): {message}")
            return render(request, 'user/thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'user/contact.html', {'form': form})
