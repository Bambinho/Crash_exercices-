from django.shortcuts import render, redirect 
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
	if request.method!='POST':
		# Make a blank  form
		form=UserCreationForm()

	else :
		#make a form fill with data 
		form=UserCreationForm(data=request.POST)
		#check if the form is valid 
		if form.is_valid :
			new_user=form.save()
			# login the user( a validated sessions)
			login(request,new_user)
			return redirect('learning_logs:index')

	#send the blank or invalid form 
	context={'form':form}
	return render(request,'registration/register.html',context)



