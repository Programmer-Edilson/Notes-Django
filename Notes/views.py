from django.shortcuts import redirect

def gateway(request):
    if request.user.is_authenticated:
        return redirect('notes')
    else:
        return redirect('login')
