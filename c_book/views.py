from django.shortcuts import render
from django.template import loader
from django.db.models import Q

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ContactForm
from .models import Contact


@login_required
def contact_add(request):
    form = ContactForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            contact = Contact()
            contact.user_id = request.user.id
            contact.name = request.POST.get('name')
            contact.contact = request.POST.get('contact')
            contact.email = request.POST.get('email')
            contact.save()
            success = True
            message = "successfully Saved !"
            return render(request, 'c_book/add.html', {'form': form, 'message':message, 'success':success})
        success = False
        message = "Failed to Save !"
        return render(request, 'c_book/add.html', {'form': form, 'success':success})
    #else get request
    return render(request, 'c_book/add.html', {'form': form})


@login_required
def get_all_contacts(request):
    contact_list = Contact.objects.filter(user__id=request.user.id)
    paginator = Paginator(contact_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'c_book/all_contacts.html', {'contacts': contacts})


@login_required
def delete_contact(request, contact_id):
    try:
        contact = Contact.objects.get(id=contact_id)
    except Contact.DoesNotExist:
        contact = None
    return render(request, 'c_book/contact_delete_confirmation.html')


@login_required
def edit_contact(request, contact_id):

    if request.method == 'POST':
        contact = Contact.objects.get(id=contact_id)
        contact.user_id = request.user.id
        contact.name = request.POST.get('name')
        contact.contact = request.POST.get('contact')
        contact.email = request.POST.get('email')
        contact.save()
        success = True
        message = "successfully Updated !"
        data = {'name' : contact.name, 'contact' : contact.contact, 'email' : contact.email, 'id':contact.id}
        form = ContactForm(initial=data)
        return render(request, 'c_book/edit.html', {'form': form, 'message':message, 'success':success})
    else:
        contact = get_object_or_404(Contact, pk=contact_id)
        if contact:
            data = {'name' : contact.name, 'contact' : contact.contact, 'email' : contact.email, 'id':contact.id}
            form = ContactForm(initial=data)
            return render(request, 'c_book/edit.html',{'form':form})
    return HttpResponse("Something went wrong")


@login_required
def edit_contact(request, contact_id):

    if request.method == 'POST':
        contact = Contact.objects.get(id=contact_id)
        contact.user_id = request.user.id
        contact.name = request.POST.get('name')
        contact.contact = request.POST.get('contact')
        contact.email = request.POST.get('email')
        contact.save()
        success = True
        message = "successfully Updated !"
        data = {'name' : contact.name, 'contact' : contact.contact, 'email' : contact.email, 'id':contact.id}
        form = ContactForm(initial=data)
        return render(request, 'c_book/edit.html', {'form': form, 'message':message, 'success':success})
    else:
        contact = get_object_or_404(Contact, pk=contact_id)
        if contact:
            data = {'name' : contact.name, 'contact' : contact.contact, 'email' : contact.email, 'id':contact.id}
            form = ContactForm(initial=data)
            return render(request, 'c_book/edit.html',{'form':form})
    return HttpResponse("Something went wrong")


@login_required
def get_search_contacts(request):

    search_key =  request.POST.get('search_key') if request.POST.get('search_key') else ""
    contact_list = []
    if search_key:
        contact_list = Contact.objects.filter( Q(name__icontains=search_key)|Q(email__icontains=search_key), user__id=request.user.id)
    paginator = Paginator(contact_list, 10) # Show 10 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'c_book/search.html', {'contacts': contacts})
