from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from contacts.models import Contact

# Create your views here.
def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been Created.')
            return redirect('login')
        else:
            messages.error(request, f'Invalid Credentials')
    else:
        form=UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})


def login(request):
    messages.success(request, f'you are now logged in')
    return render(request, "accounts/dashboard.html")

@login_required
def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts': user_contacts
    }
    return render(request, "accounts/dashboard.html", context)

@login_required
def logout(request):
    return redirect(request, "index")