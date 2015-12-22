from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext

from persons.models import Person
from persons.forms import AddPersonForm, RemovePersonForm

def index(request):
    t = loader.get_template('index.html')
    return HttpResponse(t.render(RequestContext(request, {})))

def list_persons(request):
    GET_SHORT_NAME = 'short'
    GET_FULL_NAME = 'full'
    GET_EMAIL = 'mail'

    get_params = { GET_SHORT_NAME : request.GET.get(GET_SHORT_NAME),
                    GET_FULL_NAME : request.GET.get(GET_FULL_NAME),
                    GET_EMAIL : request.GET.get(GET_EMAIL) }

    filter_strings = { GET_SHORT_NAME : 'short_name__icontains',
                        GET_FULL_NAME : 'full_name__icontains',
                        GET_EMAIL : 'email__icontains' }

    persons = Person.objects.all()    

    for param in get_params:
        print 'GET: %s = %s' % (param, get_params[param]) # for debug
        if get_params.get(param):
            filter_dict = { filter_strings[param] : get_params[param] }
            persons = persons.filter(**filter_dict)

    context_dict = {}
    context_dict['persons'] = persons
    context_dict['persons_count'] = len(persons)

    # make list font tiny:
    context_dict['tiny_font'] = request.GET.get('tiny')

    t = loader.get_template('persons.html')
    return HttpResponse(t.render(RequestContext(request, context_dict)))

def manage_persons(request):
    persons = Person.objects.all()
    form_data = request.POST if request.POST else None
    if form_data: # debug info
        print form_data # POST data (for debug)

    form_add = AddPersonForm(form_data)
    if form_add.is_valid():
        new_person = Person(
                        short_name=form_data.get('short_name'),
                        full_name=form_data.get('full_name'),
                        email=form_data.get('email')
                     )
        new_person.save() # write new row to DB
        return redirect('/persons/')

    form_rem = RemovePersonForm(form_data)
    if form_rem.is_valid():
        persons_to_be_removed = Person.objects.filter(
                    short_name__icontains=form_data.get('short_name_substr'))
        persons_to_be_removed.delete() # delete row from DB
        return redirect('/persons/')

    t = loader.get_template('manage.html')
    return HttpResponse(t.render(RequestContext(request,
                                       {'form_add' : form_add,
                                        'form_rem' : form_rem,
                                        'persons_count' : len(persons),} 
                        )))

