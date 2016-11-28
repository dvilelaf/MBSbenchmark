from django.shortcuts import render, get_object_or_404
from problems.models import Problem, User, Solution
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import contactform, problemform, solutionform, filterform
import datetime
from django.conf import settings
import logging
import shutil


def index(request):
    context = {'tab' : 'home',}
    return render(request, 'problems/index.html', context)


def faq(request):
    context = {'tab' : 'faq',}
    return render(request, 'problems/faq.html', context)


def terms(request):
    context = {'tab' : 'links',}
    return render(request, 'problems/terms.html', context)


def problemsuccess(request):
    context = {'tab' : 'submit',}
    return render(request, 'problems/problemsuccess.html', context)

def solutionsuccess(request, problem_name):
   
    problem = get_object_or_404(Problem, name = problem_name.replace('_',' '))
    context = {'problem' : problem, 
               'tab' : 'browse',}
    return render(request, 'problems/solutionsuccess.html', context)


def submitproblem(request): 

    if request.method == 'POST':

        form = problemform(request.POST, request.FILES)

        if form.is_valid():

            try:
                user = User.objects.get(email = form.cleaned_data['email'].strip())
            except User.DoesNotExist:
                user = User(name        = form.cleaned_data['username'].strip(), 
                            email       = form.cleaned_data['email'].strip(), 
                            signup_date = datetime.datetime.today())
                user.save()

            if form.cleaned_data['authors']:
                authors = form.cleaned_data['authors']
            else:
                authors = user.name

            problem = Problem(name        = form.cleaned_data['name'].strip(),      
                              user        = user,   
                              authors     = authors, 
                              sub_date    = datetime.datetime.today(),           
                              image       = form.cleaned_data['image'],        
                              description = form.cleaned_data['description'],      
                              comments    = form.cleaned_data['comments'],      
                              application = form.cleaned_data['application'],      
                              analysis    = form.cleaned_data['analysis'],      
                              contact     = form.cleaned_data['contact'],      
                              flexibility = form.cleaned_data['flexibility'],      
                              topology    = form.cleaned_data['topology'])      

            problem.save()


            solution = Solution(problem       = problem,
                                user          = user,
                                authors       = authors, 
                                sub_date      = datetime.datetime.today(),
                                accuracy      = form.cleaned_data['accuracy'],
                                cputime       = form.cleaned_data['cputime'],
                                cpu           = form.cleaned_data['cpu'],
                                os            = form.cleaned_data['os'],
                                method        = form.cleaned_data['method'],
                                results       = form.cleaned_data['results'],
                                miscellaneous = form.cleaned_data['miscellaneous'])   

            solution.save()


            shutil.move(settings.MEDIA_ROOT + 'solutions/' + solution.problem.name.lower() + '/' + solution.user.name.lower() + '/uploading',
                        settings.MEDIA_ROOT + 'solutions/' + solution.problem.name.lower() + '/' + solution.user.name.lower() + '/' + str(solution.id))

            solution.results.name = solution.results.name.replace('uploading', str(solution.id))
            if solution.miscellaneous.name:
                solution.miscellaneous.name = solution.miscellaneous.name.replace('uploading', str(solution.id))
            solution.save()

            # Send notification mails

            message = 'Dear Mr/Ms ' + user.name + ',\n\n' + \
                      'This is an automatic notification from the Multibody Benchmark website. Your proposed problem "' + problem.name + \
                      '" has been correctly submitted and should be reviewed within the next few days.\nWe will notify you ' + \
                      'again when it is incorporated to our database.\n\nBest regards.'

            email = EmailMessage(subject    = 'Multiboy Benchmark Confirmation: new problem submission', 
                                 body       =  message, 
                                 from_email = 'multibodybenchmark@gmail.com',
                                 to         = [user.email])
            email.send()

            message = 'A new problem has been submitted to the MB Benchmark database:\n\n' + \
                      'SUBMITTER:        ' + user.name                         + '\n' +\
                      'MAIL:             ' + user.email                        + '\n' +\
                      'PROBLEM NAME:     ' + problem.name                      + '\n' +\
                      'APPLICATION:      ' + problem.get_application_display() + '\n' +\
                      'FLEXIBILITY:      ' + problem.get_flexibility_display() + '\n' +\
                      'CONTACT:          ' + problem.get_contact_display()     + '\n' +\
                      'ANALYSIS:         ' + problem.get_analysis_display()    + '\n' +\
                      'TOPOLOGY:         ' + problem.get_topology_display()    + '\n' +\
                      'COMMENTS:         ' + problem.comments                  + '\n' +\
                      'ACCURACY:         ' + str(solution.accuracy)            + '\n' +\
                      'TIME:             ' + str(solution.cputime)             + '\n' +\
                      'CPU:              ' + solution.cpu                      + '\n' +\
                      'OPERATING SYSTEM: ' + solution.os                       + '\n' +\
                      'METHOD:           ' + solution.method                   + '\n\n' +\
                      'Find attached image, description file and miscellaneous file if submitted.'

            email = EmailMessage(subject    = 'New problem submission: ' + problem.name + ' by ' + user.name, 
                                 body       =  message, 
                                 from_email = 'multibodybenchmark@gmail.com',
                                 to         = ['multibodybenchmark@gmail.com',])

            email.attach_file(settings.MEDIA_ROOT + problem.image.name)
            email.attach_file(settings.MEDIA_ROOT + problem.description.name)
            email.attach_file(settings.MEDIA_ROOT + solution.results.name, 'application/octet-stream')
            if form.cleaned_data['miscellaneous']:
                email.attach_file(settings.MEDIA_ROOT + solution.miscellaneous.name)
            email.send()
            
            return HttpResponseRedirect('success/')
    else:
        form = problemform()

    sampleproblem = Problem.objects.get(name = 'Double four bar mechanism')

    context = {'form': form,
               'application_choices' : Problem.application_choices,
               'analysis_choices'    : Problem.analysis_choices,
               'contact_choices'     : Problem.contact_choices,
               'flexibility_choices' : Problem.flexibility_choices,
               'topology_choices'    : Problem.topology_choices,
               'tab'                 : 'submit',
               'sampleproblem'       : sampleproblem}

    return render(request, 'problems/submitproblem.html', context)

def submitsolution(request, problem_name):

    problem = get_object_or_404(Problem, name = problem_name.replace('_',' '))

    if request.method == 'POST':

        form = solutionform(request.POST, request.FILES)

        if form.is_valid():

            try:
                user = User.objects.get(email = form.cleaned_data['email'].strip())
            except User.DoesNotExist:
                user = User(name        = form.cleaned_data['username'].strip(), 
                            email       = form.cleaned_data['email'].strip(), 
                            signup_date = datetime.datetime.today())
                user.save()

            if form.cleaned_data['authors']:
                authors = form.cleaned_data['authors']
            else:
                authors = user.name

            solution = Solution(problem       = problem,
                                user          = user,
                                authors       = authors, 
                                sub_date      = datetime.datetime.today(),
                                accuracy      = form.cleaned_data['accuracy'],
                                cputime       = form.cleaned_data['cputime'],
                                cpu           = form.cleaned_data['cpu'],
                                os            = form.cleaned_data['os'],
                                method        = form.cleaned_data['method'],
                                results       = form.cleaned_data['results'],
                                miscellaneous = form.cleaned_data['miscellaneous'])   

            solution.save()

            shutil.move(settings.MEDIA_ROOT + 'solutions/' + solution.problem.name.lower() + '/' + solution.user.name.lower() + '/uploading',
                        settings.MEDIA_ROOT + 'solutions/' + solution.problem.name.lower() + '/' + solution.user.name.lower() + '/' + str(solution.id))

            solution.results.name = solution.results.name.replace('uploading', str(solution.id))
            if solution.miscellaneous.name:
                solution.miscellaneous.name = solution.miscellaneous.name.replace('uploading', str(solution.id))
            solution.save()


            # Send notification mails

            message = 'Dear Mr/Ms ' + user.name + ',\n\n' + \
                      'This is an automatic notification from the Multibody Benchmark website. Your solution for "' + solution.problem.name + \
                      '" has been correctly submitted and incorporated to our database.\n\nBest regards.'

            email = EmailMessage(subject    = 'Multiboy Benchmark Confirmation: new solution submission', 
                                 body       =  message, 
                                 from_email = 'multibodybenchmark@gmail.com',
                                 to         = [user.email])
            email.send()

            message = 'A new solution has been submitted to the MB Benchmark database:\n\n' + \
                      'SUBMITTER:        ' + user.name                         + '\n' +\
                      'MAIL:             ' + user.email                        + '\n' +\
                      'PROBLEM NAME:     ' + solution.problem.name             + '\n' +\
                      'ACCURACY:         ' + str(solution.accuracy)            + '\n' +\
                      'TIME:             ' + str(solution.cputime)             + '\n' +\
                      'CPU:              ' + solution.cpu                      + '\n' +\
                      'OPERATING SYSTEM: ' + solution.os                       + '\n' +\
                      'METHOD:           ' + solution.method                   + '\n\n' +\
                      'Find attached results and miscellaneous file if submitted.'

            email = EmailMessage(subject    = 'New solution submission for ' + solution.problem.name + ' by ' + user.name, 
                                 body       =  message, 
                                 from_email = 'multibodybenchmark@gmail.com',
                                 to         = ['multibodybenchmark@gmail.com',])

            email.attach_file(settings.MEDIA_ROOT + solution.results.name, 'application/octet-stream')
            if form.cleaned_data['miscellaneous']:
                email.attach_file(settings.MEDIA_ROOT + solution.miscellaneous.name)
            email.send()
            
            return HttpResponseRedirect('submit/success')
    else:
        form = problemform()

    context = {'form': form,
               'problem' : problem}

    return render(request, 'problems/submitsolution.html', context)


def browse(request):

    if request.method == 'POST':

        form = filterform(request.POST)

        if form.is_valid():

            problems = Problem.objects.filter(published = True).order_by('-sub_date')

            if form.cleaned_data['application'] != 'ANY':  problems = problems.filter(application = form.cleaned_data['application'])      
            if form.cleaned_data['analysis']    != 'ANY':  problems = problems.filter(analysis    = form.cleaned_data['analysis'])      
            if form.cleaned_data['contact']     != 'ANY':  problems = problems.filter(contact     = form.cleaned_data['contact'])      
            if form.cleaned_data['flexibility'] != 'ANY':  problems = problems.filter(flexibility = form.cleaned_data['flexibility'])      
            if form.cleaned_data['topology']    != 'ANY':  problems = problems.filter(topology    = form.cleaned_data['topology'])

            problems.order_by('-sub_date')  

            selected = {'ap' : form.cleaned_data['application'],
                        'an' : form.cleaned_data['analysis'],
                        'co' : form.cleaned_data['contact'],
                        'fl' : form.cleaned_data['flexibility'],
                        'to' : form.cleaned_data['topology']} 

    else:

        form = filterform()
        problems = Problem.objects.filter(published = True).order_by('-sub_date')

        selected = {'ap' : 'ANY',
                    'an' : 'ANY',
                    'co' : 'ANY',
                    'fl' : 'ANY',
                    'to' : 'ANY'}

    context = {'form'                : form,
               'application_choices' : Problem.application_choices,
               'analysis_choices'    : Problem.analysis_choices,
               'contact_choices'     : Problem.contact_choices,
               'flexibility_choices' : Problem.flexibility_choices,
               'topology_choices'    : Problem.topology_choices,
               'problems'            : problems,
               'tab'                 : 'browse',}

    context.update(selected)


    return render(request, 'problems/browse.html', context)


def problem(request, problem_name):
    problem = get_object_or_404(Problem, name = problem_name.replace('_',' '))
    solutions = Solution.objects.filter(problem = problem).order_by('sub_date')
    context = {'problem': problem,
               'ref_solution' : solutions[0],
               'solutions': solutions[1:],
               'tab' : 'browse',}

    return render(request, 'problems/problem.html', context)

def solution(request, solution_id):
    context = {'solution': get_object_or_404(Solution, pk = solution_id),
              'tab' : 'browse',}
    return render(request, 'problems/solution.html', context)


def contactsuccess(request):
    context = {'tab' : 'contact',}
    return render(request, 'problems/contactsuccess.html', context)


def contact(request):

    if request.method == 'POST':

        form = contactform(request.POST)

        if form.is_valid():

            message = form.cleaned_data['name'] + ' (' + form.cleaned_data['email'] + ') ' + 'has submitted the following message to the MB Benchmark site:\n\n' + form.cleaned_data['message']

            email = EmailMessage(subject    = 'New Contact Form', 
                                 body       =  message, 
                                 from_email = 'multibodybenchmark@gmail.com',
                                 to         = ['multibodybenchmark@gmail.com',])

            email.send()

            return HttpResponseRedirect('success/')
    else:
        form = contactform()

    context = {'tab' : 'contact',
               'form': form,}

    return render(request, 'problems/contact.html', context)


def zagreb13(request):
    context = {'tab': 'links'}
    return render(request, 'problems/zagreb13.html', context)

