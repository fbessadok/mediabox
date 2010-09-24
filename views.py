from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render_to_response('home.html', {}, RequestContext(request))

# eof
