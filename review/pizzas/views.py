from django.shortcuts import render

# Create your views here.

from . models import Pizza 

def index(request):

	return render(request,'pizzas/index.html')


def pizzas(request):

	pizzas=Pizza.objects.all()
	context={'pizzas':pizzas}
	return render(request,'pizzas/pizzas.html',context)
def toppings(request,top_id):
	pizza=Pizza.objects.get(id=top_id)
	toppings=pizza.topping_set.order_by('-date_added')
	context={'pizza':pizza,'toppings':toppings}
	return render(request,'pizzas/toppings.html',context)
