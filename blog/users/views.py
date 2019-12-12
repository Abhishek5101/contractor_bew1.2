from django.shortcuts import render
from .forms import RegisterationForm


def register(request):
	if request.method == 'POST':
		form = RegisterationForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = RegisterationForm()
		
	context = {'form': form}
	return render(request, 'users/register.html', context)