from django.shortcuts import render,render_to_response,RequestContext,HttpResponseRedirect
# Create your views here.
from django.contrib import messages
from .forms import SignUpForm
def home(request):
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		save_it =form.save(commit=False)
		save_it.save()
		messages.success(request,'Submitted !')
		return HttpResponseRedirect('/Submitted/')
	return render_to_response("signup.html",
								locals(),
								context_instance=RequestContext(request))

def Submitted(request):
	
	return render_to_response("Submitted.html",
								locals(),
								context_instance=RequestContext(request))