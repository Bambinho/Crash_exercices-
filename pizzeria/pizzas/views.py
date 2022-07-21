from django.shortcuts import render,redirect
from . models import Pizza,Topping 
from . forms import PizzaForm , ToppingForm
from django.contrib.auth.decorators import login_required 
from django.http import Http404

# Create your views here.

def check_pizza_owner(request,pizza):
	if request.user!=pizza.owner:
		raise Http404





def index(request):

	return render(request,'pizzas/index.html')




@login_required
def pizzas(request):
	pizzas=Pizza.objects.order_by('date_added')
	context={'pizzas':pizzas}
	return render(request,'pizzas/pizzas.html',context)

@login_required
def topping(request,pizza_id):
	pizza=Pizza.objects.get(id=pizza_id)
	check_pizza_owner(request,pizza)
	toppings=pizza.topping_set.order_by('-date_added')
	context={'pizza':pizza,'toppings':toppings}
	return render(request,'pizzas/topping.html',context)

def new_pizza(request):

	if request.method !='POST':
		#make an empty form 
		form=PizzaForm()
	else:
		#proccess the fill form
		form=PizzaForm(data=request.POST)
		if form.is_valid:
			new_pizza=form.save(commit=False )
			new_pizza.owner=request.user
			new_pizza.save()
			return redirect('pizzas:pizzas')

	context={'form':form}

	return render(request,'pizzas/new_pizza.html',context)




def new_top(request,pizza_id):
	pizza=Pizza.objects.get(id=pizza_id)
	check_pizza_owner(request,pizza)
	if request.method !='POST':
		##Blank form 
		form=ToppingForm()
	else:
		form=ToppingForm(data=request.POST)
		if form.is_valid:
			new_top=form.save(commit=False)
			new_top.pizza=pizza
			new_top.pizza.owner=request.user 
			new_top.save()
			return redirect('pizzas:topping',pizza_id)

	context={'form':form,'pizza':pizza}
	return render(request,'pizzas/new_top.html',context)

def edit_top(request,top_id):

	top=Topping.objects.get(id=top_id)
	pizza=top.pizza
	check_pizza_owner(request,pizza)
	if request.method!='POST':
		##Blank from 
		form=ToppingForm(instance=top)

	else:
		#Process form 
		form=ToppingForm(instance=top,data=request.POST)
		if form.is_valid:
			#form.save(commit=False)
			#form.pizza=pizza
			form.save()
			return redirect('pizzas:topping',pizza.id)

	context={'form':form,'top':top,'pizza':pizza}

	return render(request,'pizzas/edit_top.html',context)









