from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from doc.models import DocPub
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    file_list=DocPub.objects.all()
    return render_to_response('doc/index.html',{'file_list':file_list},context_instance=RequestContext(request))

@login_required
def add_file(request):
    return render_to_response('doc/addfile.html',{},context_instance=RequestContext(request))