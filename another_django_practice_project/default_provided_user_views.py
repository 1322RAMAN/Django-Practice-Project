from .default_provided_user_forms import UserRegisstreationForm, ContactMailForm, UserLogin, SuperuserCreationForm
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.core.mail import send_mail
# from .tasks import add, send_email_task
from user.tasks import send_welcome_email_task


def home(request):
    return render(request, 'home.html', {'name': request.user})


def register_user(request):
    if request.method == 'POST':
        form = UserRegisstreationForm(request.POST)  # Handle POST data
        if form.is_valid():  # Validate the input
            form.save()  # Save valid data to the database
            return redirect('user_login')  # Redirect to login page
    else:
        form = UserRegisstreationForm()  # Render an empty form for GET request
    return render(request, 'register_user.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)  # Handle POST data
        if form.is_valid():  # Validate the input
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Authenticate the user
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                # return redirect('welcome')  # Redirect to the welcome page
                next_url = request.POST.get('next', 'welcome')  # Default to 'welcome' if 'next' is not present
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")  # Show error for invalid credentials
    else:
        form = UserLogin()  # Render an empty form for GET request

    # Get the 'next' parameter from the query string to pass it to the form
    # next_url = request.GET.get('next', '')
    next_url = request.GET.get('next', '/welcome/')  # Default to '/welcome/' if not present
    return render(request, 'user_login.html', {'form': form, 'next': next_url})
    # return render(request, 'user_login.html', {'form': form})


@login_required
# @user_passes_test(lambda u: u.is_superuser)  # Only allow current superusers
def create_superuser(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            # Check if the username already exists
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                # If the username exists, show an error message or handle accordingly
                messages.error(request, f"User with username '{username}' already exists.")
                return render(request, 'create_superuser.html', {'form': form})

            # Proceed with form save if no duplicates
            form.save()
            return redirect('home')  # Redirect to a success page
        else:
            # Loop through the form fields to display validation errors
            for field in form:
                if field.errors:
                    for error in field.errors:
                        messages.error(request, f"{field.label}: {error}")

    else:
        form = SuperuserCreationForm()
    return render(request, 'create_superuser.html', {'form': form})


def get_user_details(request):
    # user_details = User.objects.all()   # Fetch all user objects
    # user_details2 = User.objects.all().values()
    # return render(request, 'user_details.html', {'user_details': user_details})

    users = User.objects.all()  # Fetch all user objects
    # user_fields = [field.name for field in User._meta.fields]  # Get all field names
    user_fields = [field.name for field in User._meta.get_fields()]
    # return render(request, 'user_details.html', {'users': users, 'user_fields': user_fields})
    return render(request, 'user_details.html', {'users': users, 'user_fields': user_fields})


def contact_view(request):
    if request.method == 'POST':
        form = ContactMailForm(request.POST)
        if form.is_valid():
            form.save()  # Calls the save() method defined in the form
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ContactMailForm()

    return render(request, 'contact.html', {'form': form})


@login_required
def success(request):
    return HttpResponse('<h1>Successfully Sent Email</h1>')


@login_required
def welcome(request):
    return render(request, 'welcome.html')


@login_required
def logout_user(request):
    logout(request)
    messages.get_messages(request).used = True  # Clear all messages
    messages.success(request, "You have successfully logged out.")  # Optional logout message
    return redirect('user_login')


@login_required
@user_passes_test(lambda u: u.is_superuser)  # Restrict access to current superusers
def make_superuser(request, username):
    try:
        user = User.objects.get(username=username)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        messages.success(request, f"{user.username} have successfully created Superuser.")
        return redirect('welcome')  # Redirect to a success page
    except User.DoesNotExist:
        return redirect('welcome')  # Handle the error as needed


# def test_task(request):
#     result = add.delay(10, 20)  # Asynchronous execution
#     return JsonResponse({"task_id": result.id})


def send_email_view(request):
    send_mail(
        subject="Test Sendgrid Email - Hello from Django",
        message="This is a test email sent via SendGrid from your Django project.",
        from_email="ramandhiman1322@gmail.com",  # Replace with your email.
        recipient_list=["1322noobmaster@gmail.com"],  # Replace with the recipient's email.
    )
    return HttpResponse("Email Sent")


def send_email_view2(request):
    subject = "Welcome to My App"
    message = "Thank you for signing up!"
    from_email = "ramandhiman1322@gmail.com"
    recipient_list = ["1322noobmaster@gmail.com"]

    # Call the Celery task to send the email
    # send_email_task.delay(subject, message, from_email, recipient_list)
    send_welcome_email_task.delay(subject, message, from_email, recipient_list)

    return JsonResponse({"message": "Email task initiated successfully!"})
