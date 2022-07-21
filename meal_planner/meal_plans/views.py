from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Day,Meal
from .forms import MealForm,DayForm
from django.http import Http404

def check_owner_meal(request,day):
	if request.user!=day.owner:
		raise Http404


# Create your views here.

def index(request):
	return render(request,'meal_plans/index.html')

@login_required
def day(request):
	days=Day.objects.filter(owner=request.user).order_by('-date_added')
	context={'days':days}
	return render(request,'meal_plans/days.html',context)

def new_day(request):

	if request.method!='POST':
		form=DayForm()
	else:
		form=DayForm(data=request.POST)

		if form.is_valid:
			new_day=form.save(commit=False)
			new_day.owner=request.user 
			new_day.save()
			return redirect('meal_plans:day')
	context={'form':form }

	return render(request,'meal_plans/new_day.html',context)


@login_required
def meals(request,day_id):
	day=Day.objects.get(id=day_id)
	check_owner_meal(request,day)
	meals=day.meal_set.order_by('-date_added')
	context={'day':day,'meals':meals}
	return render(request,'meal_plans/meals.html',context)

@login_required
def new_meal(request,day_id):

	day=Day.objects.get(id=day_id)
	check_owner_meal(request,day)
	if request.method!='POST':
		#form=MealForm(instance=day)
		form=MealForm()
		
	else :
		form=MealForm(data=request.POST)
		if form.is_valid:
			new_meal=form.save(commit=False)
			new_meal.day=day
			new_meal.owner=request.user
			new_meal.save()
			#form.save()
		return redirect('meal_plans:meals',day_id)

	context={'form':form,'day':day}

	return render(request,'meal_plans/new_meal.html',context)



@login_required
def edit_meal(request, meal_id):

	meal=Meal.objects.get(id=meal_id)
	day=meal.day
	check_owner_meal(request,day)

	if request.method!='POST':
		#Empty Form 
		form=MealForm(instance=meal)

	else:
		form=MealForm(instance=meal,data=request.POST)

		if form.is_valid:
			form.save()
			return redirect('meal_plans:meals',day.id)

	context={'form':form,'day':day,'meal':meal}

	return render(request,'meal_plans/edit_meal.html',context)





