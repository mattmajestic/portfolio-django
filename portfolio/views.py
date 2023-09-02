from django.shortcuts import render
from django.http import HttpResponseRedirect
from portfolio.forms import ContactForm
from portfolio.models import Contact
from django.urls import reverse


def home(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save() 
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('thanks',))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
