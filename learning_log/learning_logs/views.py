from django.shortcuts import render

# Create your views here.
from . models import Topic 

def index(request):
	"""The home page for learning Log."""
	return render(request,'learning_logs/index.html')

def topics(request):
	"""Show all topics"""
	topics=Topic.objects.order_by('date_added')
	context={'topics': topics}
	return render(request,'learning_logs/topics.html',context)

def topic(request,topic_id):
	"""show  a specific topic with entries"""
	topic=Topic.objects.get(id=topic_id)
	entries=topic.entry_set.order_by('-date_added')
	context={'topic':topic,'entries':entries}

	return render(request,'learning_logs/topic.html',context)


