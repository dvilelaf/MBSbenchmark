from django.contrib import admin
from problems.models import Problem, Solution, User
import os

class ProblemAdmin(admin.ModelAdmin):
    
    def user_name(self, instance):
        return instance.user.name

    list_display = ('id', 'name', 'user_name', 'authors', 'published', 'sub_date', 'application', 'topology', 'flexibility', 'analysis', 'contact') 


class SolutionAdmin(admin.ModelAdmin):

    def user_name(self, instance):
        return instance.user.name

    def problem_name(self, instance):
        return instance.problem.name

    list_display = ('id', 'problem_name', 'user_name', 'authors') 


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'signup_date', 'numproblems', 'numsolutions',) 

    def numproblems(self, obj):
        return len(Problem.objects.filter(user = obj))

    def numsolutions(self, obj):
        return len(Solution.objects.filter(user = obj))


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(User, UserAdmin)
