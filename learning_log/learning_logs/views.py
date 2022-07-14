from django.shortcuts import render,redirect 

# Create your views here.
from .models import Topic,Entry
from .forms import TopicForm, EntryForm



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

def new_topic(request):
	"""Add a new topic """
	if request.method!='POST':
		#No data submitted; creat a blank form.
		form=TopicForm()

	else:
		#POST data submitted; proccess data 
		form=TopicForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topics')

	#Display a blank or invalid forms.
	context={'form':form}
	return render(request,'learning_logs/new_topic.html',context)


def new_entry(request,topic_id):

	topic=Topic.objects.get(id=topic_id)
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


def edit_entry(request,entry_id):
	"""Edit entry view """
	entry=Entry.objects.get(id=entry_id)
	topic=entry.topic 

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







