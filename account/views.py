from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth import authenticate,login,logout
from DepOA.views import index

def login_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return index(request)
    else:
        return index(request)

def logout_view(request):
    logout(request)
    return index(request)