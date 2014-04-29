from django.shortcuts import render_to_response
from django.template import loader, Context,RequestContext

from django.http import HttpResponse
from stories.models import Story

# Create your views here.

def top_stories():
	latest_stories=Story.objects.all().order_by('-created_at');
	return latest_stories

def index(request):
	stories=top_stories();
	# template=loader.get_template('index.html')
	context=RequestContext(request,{'stories' : stories})
	# response=template.render(context)
	# return HttpResponse(response)
	return render_to_response('index.html', {'stories' : stories}) 
