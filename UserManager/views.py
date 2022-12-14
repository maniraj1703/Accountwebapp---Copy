from django.shortcuts import render, redirect, get_object_or_404
from UserManager.models import UserManager
from UserManager.forms import SigupForm
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect

# Create your views here.
def signup_view(request):
    form = SigupForm()
    if request.method == 'POST':
        form = SigupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return redirect("login")
    return render(request,'UserInterface/signup.html', { 'form':form })








