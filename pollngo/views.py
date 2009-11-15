from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from models import *
import pforms
from pygooglechart import PieChart2D

def index(request):
    return render('pollngo/index.html', {}, request)

def question(request, slug):
    try:
        question = Question.objects.get(slug = slug)
    except ObjectDoesNotExist, e:
        raise Http404    
    if request.method == 'POST':
        try:
            last_choice_id = request.session[question.id]
            last_choice = Choice.objects.get(id = last_choice_id)
            last_choice.total_votes -= 1
            last_choice.save()
        except KeyError, e:
            pass        
        choice_id = int(request.POST['choices'])
        choice = Choice.objects.get(id = choice_id)
        choice.total_votes += 1
        choice.save()
        request.session[question.id] = choice.id
        return HttpResponseRedirect(question.get_results_url())
    if request.method == 'GET':
        try:
            last_choice_id = request.session[question.id]
            last_choice = Choice.objects.get(id = last_choice_id)
        except KeyError, e:
            last_choice = 0
        choices = Choice.objects.filter(question = question)
        payload = {'question':question, 'choices':choices, 'last_choice':last_choice}
        
        return render('pollngo/question.html', payload, request)

def results(request, slug):
    try:
        question = Question.objects.get(slug = slug)
    except ObjectDoesNotExist, e:
        raise Http404
    total_votes = 0
    choice_name = []
    choice_val = []
    for choice in question.choice_set.all():
        total_votes += choice.total_votes
        choice_name.append(choice.text)
        choice_val.append(choice.total_votes)
    chart = PieChart2D(400, 200)
    chart.add_data(choice_val)
    choice_name = [choice_obj.encode('utf8') for choice_obj in choice_name]
    chart.set_pie_labels(choice_name)
    chart_url = chart.get_url()    
    payload = {'question':question, 'total_votes':total_votes, 'chart_url':chart_url}
    return render('pollngo/results.html', payload, request)
        
    

def create(request):
    if request.method == 'POST':    
        form = pforms.CreatePoll(request, request.POST)
        if form.is_valid():
            question = form.save()
            try:
                questions = request.session['questions']
            except KeyError, e:
                questions = []
            questions.append(question.id)
            request.session['questions'] = questions
            return HttpResponseRedirect(question.get_absolute_url())
    elif request.method == 'GET':
        form = pforms.CreatePoll(request)
    payload = {'form':form}
    return render('pollngo/create.html', payload, request)

def help(request):
    payload = {}
    return render('pollngo/help.html', payload, request)
    
#Helper methods.
def render(template_name, payload, request):
    recent_polls = Question.objects.all()[:8]
    try:
        questions = request.session['questions']
    except KeyError, e:
        questions = []
    your_polls = Question.objects.filter(id__in = questions)
    payload.update({'recent_polls':recent_polls, 'your_polls':your_polls})
    return render_to_response(template_name, payload, RequestContext(request))
    


