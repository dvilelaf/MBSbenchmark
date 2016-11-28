from django.db import models

class User(models.Model):

    name        = models.CharField(max_length = 64)
    email       = models.EmailField()
    signup_date = models.DateTimeField('date signup')

    def __str__(self):
        return self.name

def get_problem_path(instance, filename):
    return 'problems/' + instance.name.lower() + '/' + instance.name.lower() + '.' + filename.split(".")[-1]

class Problem(models.Model):

    name      = models.CharField(max_length = 256)
    user      = models.ForeignKey(User, default=-1)
    authors   = models.CharField(max_length = 256)
    published = models.BooleanField(default = False)
    sub_date  = models.DateTimeField('date submitted')

    image       = models.ImageField(upload_to = get_problem_path)
    description = models.FileField(upload_to = get_problem_path, max_length = 500)

    comments = models.TextField(blank=True, max_length = 1024)

    #CLASSIFICATION BY APPLICATION---------------------------------------------------
    application_choices = (
            ('Aerospace Engineering',            
                (
                    ('LG','Aircraft landing gear'),
                    ('HB','Helicopter blades'),
                    ('LV','Launch vehicle dynamics'),
                    ('SS','Satellites and space structures'),
                    ('SR','Space robotics')
                )
            ),
     
            ('Automotive Dynamics',              
                (
                    ('SS','Suspension systems'),
                    ('TC','Torque converters'),
                    ('TC','Transmission components'),
                    ('VM','Vehicle dynamical models')
                )
            ),
     
            ('Biomechanical Models',             
                (
                    ('HM','Human-machine models'),
                    ('MM','Musculoskeletal models')
                )
            ),

            ('Didactic Models',                  
                (
                    ('GY','Gyrocompasses'),
                    ('MS','Mass-spring systems'),
                    ('PE','Pendula')
                )
            ),

            ('Marine Systems',                   
                (
                    ('OM','Octopus-like manipulators'),
                    ('RF','Robotic fish'),
                    ('UV','Underwater vehicles')
                )
            ),

            ('Mechanisms and Machinery',         
                (
                    ('CD','Cable-driven mechanisms'),
                    ('CL','Cam-linkage mechanisms'),
                    ('GC','Gears, chains, and pulleys'),
                    ('LK','Linkages'),
                    ('WT','Wind turbines')
                )
            ),

            ('Musical Instruments',              
                (
                    ('HA','Harpsichord action mechanisms'),
                    ('PA','Piano action mechanisms')
                )
            ),

            ('Particle and Molecular Dynamics',  
                (
                    ('FD','Fluid-multibody dynamics interaction'),
                    ('GM','Granular media modeling'),
                    ('PM','Protein models')
                )
            ),

            ('Railroad Systems',                 
                (
                    ('RD','Railroad vehicle dynamics'),
                    ('RS','Railroad vehicle suspensions'),
                    ('TP','Trolley poles')
                )
            ),

            ('Robotics',                         
                (
                    ('PR','Parallel robots'),
                    ('SR','Serial robots'),
                    ('WR','Walking robots'),
                    ('WR','Wheeled robots')
                )
            ),

            ('Sport Applications',               
                (
                    ('AR','Archery'),
                    ('BD','Bicycle dynamics'),
                    ('CL','Climbing'),
                    ('GL','Golf'),
                    ('GY','Gymnastics'),
                    ('HK','Hockey')
                )
            )        
    )
            
    #CLASSIFICATION BY CHARACTERISTIC-------------------------------------------------

    analysis_choices = (
           ('FD', 'Forward Dynamic'),
           ('ID', 'Inverse Dynamic'),
           ('KI', 'Kinematic'),
           ('ST', 'Static'),
           ('LI', 'Linearization'),
      )


    contact_choices = (
           ('CT', 'With Contact'),
           ('NC', 'Without Contact'),
      )


    flexibility_choices = (
           ('FL', 'Flexible'),
           ('RI', 'Rigid'),
      )


    topology_choices = (
           ('CL', 'Closed-loop'),
           ('OP', 'Open-loop'),
      )

    application = models.CharField(max_length = 2, choices = application_choices)
    analysis    = models.CharField(max_length = 2, choices = analysis_choices)
    contact     = models.CharField(max_length = 2, choices = contact_choices)
    flexibility = models.CharField(max_length = 2, choices = flexibility_choices)
    topology    = models.CharField(max_length = 2, choices = topology_choices)


    def __str__(self):
        return self.name


def get_solution_misc_path(instance, filename):
    return 'solutions/' + instance.problem.name.lower() + '/' + instance.user.name.lower() + '/' + \
    'uploading/miscellaneous' + '.' + filename.split(".")[-1]

def get_solution_results_path(instance, filename):
    return 'solutions/' + instance.problem.name.lower() + '/' + instance.user.name.lower() + '/' + \
    'uploading/results.txt'


class Solution(models.Model):


    problem     = models.ForeignKey(Problem)
    user        = models.ForeignKey(User)
    authors     = models.CharField(max_length = 256)
    sub_date    = models.DateTimeField('date published')

    accuracy    = models.FloatField()
    cputime     = models.FloatField()
    cpu         = models.CharField(max_length = 64)
    os          = models.CharField(max_length = 64)
    method      = models.TextField(max_length = 1024)

    results       = models.FileField(upload_to = get_solution_results_path, max_length = 500)
    miscellaneous = models.FileField(blank = True, upload_to = get_solution_misc_path, max_length = 500)

    def __str__(self):
        return self.problem.name + '-' + self.user.name + '-' + str(self.id)
    
