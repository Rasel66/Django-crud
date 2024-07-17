from django.shortcuts import render,redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'webapp/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully!")
            return redirect("login")
        
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)


#login user

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                messages.success(request, "Login successfull!")
                return redirect("dashboard")

    context = {'form': form}
    return render(request, 'webapp/login.html', context=context)


# user logout

def logout(request):
    auth.logout(request)

    messages.success(request, "Logout Success!")
    return redirect("login")

# Dashboard
@login_required(login_url='login')
def dashboard(request):

    records = Record.objects.all()
    context = {'records': records}

    return render(request, 'webapp/dashboard.html', context=context)

# Create a record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Record is created!")
            return redirect("dashboard")
        
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context=context)

# Update a record
@login_required(login_url='login')
def update_record(request,pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()

            messages.success(request, "Record updated successfully!")
            return redirect("dashboard")
    
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context=context)

# Read or view a record

@login_required(login_url='login')
def singleRecord(request, pk):
    all_records = Record.objects.get(id=pk)

    context = {"record": all_records}

    return render(request, 'webapp/view-record.html', context=context)

# Delete user
@login_required(login_url='login')
def delete_user(request, pk):
    user = Record.objects.get(id=pk)
    user.delete()
    
    messages.success(request, "Record is deleted!")
    return redirect("dashboard")
