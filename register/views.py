from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                    username=request.POST['username'],
                    password=request.POST['password1']
            )
            if user is not None:
                login(request, user)
                return redirect('notes')
            else:
                return redirect('login')
        else:
            form = UserForm(initial={
                'first_name': request.POST['first_name'],
                'last_name' : request.POST['last_name'],
                'username' : request.POST['username'],
                'email' : request.POST['email']
            })
            
            messages.warning(request, "Try a different username and password")
            context = {'form': form}
            return render(request, 'signup.html', context)
    else:
        form = UserForm()
        context = {'form': form}
        return render(request, 'signup.html', context)

@login_required
def delete(request):
    user = User.objects.get(username=request.user.username)
    
    if user is not None:
        user.delete()
        messages.success(request, "Account deleted successfully!")
        return redirect('login')
    else:
        messages.warning(request, "Error deleting account")
        return redirect('profile')

