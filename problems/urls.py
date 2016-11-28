from django.conf.urls import patterns, url
from problems import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
		  url(r'^$',                                              views.index,           name = 'index'),
		  url(r'^faq/$',                                          views.faq,             name = 'faq'),
		  url(r'^terms/$',                                        views.terms,           name = 'terms'),
		  url(r'^browse/$',                                       views.browse,          name = 'browse'),
		  url(r'^zagreb13/$',                                     views.zagreb13,        name = 'zagreb13'),
		  url(r'^contact/$',                                      views.contact,         name = 'contact'),
		  url(r'^contact/success/$',                              views.contactsuccess,  name = 'contactsuccess'),
		  url(r'^submit/$',                                       views.submitproblem,   name = 'submitproblem'),
		  url(r'^submit/success/$',                               views.problemsuccess,  name = 'problemsuccess'),
		  url(r'^problem/(?P<problem_name>\S+)/$',                views.problem,         name = 'problem'),
		  url(r'^problem/(?P<problem_name>\S+)/submit$',          views.submitsolution,  name = 'submitsolution'),
		  url(r'^problem/(?P<problem_name>\S+)/submit/success$',  views.solutionsuccess, name = 'solutionsuccess'),
		  url(r'^solution/(?P<solution_id>\d+)/$',                views.solution,        name = 'solution'),
		  #url(r'^search/$', views.search, name = 'search'),
)

