from django.shortcuts import render
from django.http import HttpResponseRedirect

"""
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/index.html')
"""
def home_view(request):
    return render(request, 'Base/home.html')

"""
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'Admin/adminclick.html')
    """