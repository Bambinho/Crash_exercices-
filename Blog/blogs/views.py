from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import PostForm 
from django.http import Http404

# Create your views here.

def index(request):
	posts=BlogPost.objects.order_by('-date_added')
	context={'posts':posts}
	return render(request,'blogs/index.html',context)


@login_required
def new_post(request):

	if request.method!='POST':
		##Return blank 
		form=PostForm()
	else:
		# Form not empty 
		form=PostForm(data=request.POST)
		if form.is_valid:
			new_post=form.save(commit=False)
			new_post.owner=request.user
			new_post.save()
			return redirect('blogs:index')

	context={'form':form }

	return render(request,'blogs/new_post.html',context)


@login_required
def edit_post(request,post_id):

	post=BlogPost.objects.get(id=post_id)

	if request.method !='POST':
		form=PostForm(instance=post)
	else:
		form=PostForm(instance=post,data=request.POST)

		#Make sure register user is editing their own page 
		if request.user != post.owner:
			raise Http404

		if form.is_valid:
			form.save()
			return redirect('blogs:index')

	context={'form':form,'post':post}

	return render(request,'blogs/edit_post.html',context)





