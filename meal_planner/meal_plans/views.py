from django.shortcuts import render

from .models import Day

# Create your views here.

def index(request):
	return render(request,'meal_plans/index.html')

def day(request):
	days=Day.objects.all()
	context={'days':days}
	return render(request,'meal_plans/days.html',context)

def meals(request,day_id):
	day=Day.objects.get(id=day_id)
	meals=day.meal_set.order_by('-date_added')
	context={'day':day,'meals':meals}
	return render(request,'meal_plans/meals.html',context)

