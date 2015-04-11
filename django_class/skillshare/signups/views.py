from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from .forms import SignUpForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):

	form = SignUpForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		subject = "Thanks"
		message = "Welcome to my site."
		from_email = settings.EMAIL_HOST_USER
		to_list = [save_it.email, "garyfimo@gmail.com"]

		send_mail(subject,message, from_email, to_list, fail_silently=True)
		messages.success(request,'Profile save success')
		return HttpResponseRedirect('/thanks')
	return render_to_response("signup.html", 
							locals(), 
				context_instance=RequestContext(request))

def thanks(request):

	return render_to_response("thanks.html", 
							locals(), 
				context_instance=RequestContext(request))

def aboutus(request):

	return render_to_response("about-us.html", 
							locals(), 
				context_instance=RequestContext(request))