from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import MessageForm
from models import Message

def message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            ip = request.META['REMOTE_ADDR']
            m = Message(name=name,
                email=email,
                title=title,
                content=content,
                ip=ip)
            m.save()
            return HttpResponseRedirect('/message/')
    else:
        form = MessageForm()
    messages = Message.objects.all().order_by('-time')
    return render_to_response('messages/message.html',
            {'form':form,'messages':messages},context_instance=RequestContext(request))
