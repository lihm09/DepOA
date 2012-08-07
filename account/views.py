from django.shortcuts import get_object_or_404, render_to_response

def login(request):
    return render_to_response('account/login.html')