from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from doc.models import DocPub

def index(request):
    return render_to_response('doc/index.html',{},context_instance=RequestContext(request))