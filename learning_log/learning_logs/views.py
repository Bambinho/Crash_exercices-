from django.shortcuts import render,redirect 

from django.contrib.auth.decorators import login_required 

# Create your views here.
from .models import Topic,Entry
from .forms import TopicForm, EntryForm
from django.http import Http404


def check_topic_owner(request,topic):

	if topic.owner!=request.user:

		raise Http404



def index(request):
	"""The home page for learning Log."""
	return render(request,'learning_logs/index.html')

@login_required 
def topics(request):
	"""Show all topics"""
	topics=Topic.objects.filter(owner=request.user).order_by('date_added')
	context={'topics': topics}
	return render(request,'learning_logs/topics.html',context)

@login_required 
def topic(request,topic_id):
	"""show  a specific topic with entries"""

	#Make sure the topic belongs to the current user.
	# if topic.owner!=request.user:
	# 	raise.Http404
	topic=Topic.objects.get(id=topic_id)
	check_topic_owner(request,topic)

	entries=topic.entry_set.order_by('-date_added')
	context={'topic':topic,'entries':entries}

	return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
	"""Add a new topic """
	if request.method!='POST':
		#No data submitted; creat a blank form.
		form=TopicForm()
	else:
		#POST data submitted; proccess data 
		form=TopicForm(data=request.POST)
		if form.is_valid():
			new_topic=form.save(commit=False)
			new_topic.owner=request.user
			new_topic.save()
			return redirect('learning_logs:topics')

	#Display a blank or invalid forms.
	context={'form':form}
	return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):

	topic=Topic.objects.get(id=topic_id)
	check_topic_owner(request,topic)
	if request.method!='POST':
		# Show blank space
		form=EntryForm()

	else:
		form=EntryForm(data=request.POST)
		if form.is_valid:
			new_entry=form.save(commit=False)
			new_entry.topic=topic 
			new_entry.save()
			return redirect('learning_logs:topic',topic_id=topic.id)

	#Display blank or invalid message

	context={'topic':topic,'form':form}
	return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
	"""Edit entry view """
	entry=Entry.objects.get(id=entry_id)
	topic=entry.topic 

#check if the current user is the user logged in 
	# if request.user!=topic.owner:
	# 	raise.Http404

	check_topic_owner(request,topic)


	if request.method!='POST':
		#show blank form 
		form=EntryForm(instance=entry)
	else:
		form=EntryForm(instance=entry,data=request.POST)
		if form.is_valid:
			form.save()
			return redirect('learning_logs:topic',topic_id=topic.id)

	context={'form':form,'topic':topic,'entry':entry}

	return render(request,'learning_logs/edit_entry.html',context)







