from django import forms 
from .models import Meal ,Day


class MealForm(forms.ModelForm):
	class Meta:
		model=Meal 
		fields=['meal_name']
		labels={'meal':''}

class DayForm(forms.ModelForm):
	class Meta:
		model=Day
		fields=['day_name']
		labels={'day_name':''}





