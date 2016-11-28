from django import forms
from problems.models import Problem

class contactform(forms.Form):

    name          = forms.CharField(label   = 'Name',                     required = True)
    email         = forms.CharField(label   = 'Email',                    required = True)
    message       = forms.CharField(label   = 'Message',                  required = True)


class problemform(forms.Form):

    username      = forms.CharField(label   = 'Name',                     required = True)
    email         = forms.CharField(label   = 'Email',                    required = True)
    authors       = forms.CharField(label   = 'Authors',                  required = False)

    name          = forms.CharField(label   = 'Problem name',             required = True)
    application   = forms.CharField(label   = 'Application',              required = True)
    topology      = forms.CharField(label   = 'Topology',                 required = True)
    analysis      = forms.CharField(label   = 'Analysis',                 required = True)
    contact       = forms.CharField(label   = 'Contact',                  required = True)
    flexibility   = forms.CharField(label   = 'Flexibility',              required = True)
    image         = forms.ImageField(label  = 'Image (png)',              required = True)    
    description   = forms.FileField(label   = 'Description file (pdf)',   required = True)
    comments      = forms.CharField(label   = 'Comments',                 required = False)
    
    accuracy      = forms.FloatField(label  = 'Accuracy',                 required = True)
    cputime       = forms.FloatField(label  = 'Cpu time',                 required = True)
    cpu           = forms.CharField(label   = 'CPU / GPU',                required = True)
    os            = forms.CharField(label   = 'Operating System',         required = True)
    method        = forms.CharField(label   = 'Method description',       required = True)
    results       = forms.FileField(label   = 'Results (txt)',            required = True)
    miscellaneous = forms.FileField(label   = 'Miscellaneous file (zip)', required = False)

    def clean_name(self):
        try:
            duplicated = Problem.objects.get(name = self.cleaned_data['name'])
        except Problem.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("This problem already exists in the library. Choose another name or submit your solution to the existing problem.")
        return self.cleaned_data['name']

    def clean_image(self):
        image = self.cleaned_data['image']
        if not image.name.endswith('.png'):
            raise forms.ValidationError("The image must be in png format.")
        return image

    def clean_description(self):
        description = self.cleaned_data['description']
        if not description.name.endswith('.pdf'):
            raise forms.ValidationError("The description file must be in pdf format.")
        return description

    def clean_results(self):
        results = self.cleaned_data['results']
        if not results.name.endswith('.txt'):
            raise forms.ValidationError("The results file must be in txt format.")
        return results

    def clean_miscellaneous(self):
        miscellaneous = self.cleaned_data['miscellaneous']
        if miscellaneous:
            if not miscellaneous.name.endswith('.zip'):
                raise forms.ValidationError("The miscellaneous file must be in zip format.")
            return miscellaneous


class solutionform(forms.Form):

    username      = forms.CharField(label   = 'Name',                     required = True)
    email         = forms.CharField(label   = 'Email',                    required = True)
    authors       = forms.CharField(label   = 'Authors',                  required = False)
 
    accuracy      = forms.FloatField(label  = 'Accuracy',                 required = True)
    cputime       = forms.FloatField(label  = 'Cpu time',                 required = True)
    cpu           = forms.CharField(label   = 'CPU / GPU',                required = True)
    os            = forms.CharField(label   = 'Operating System',         required = True)
    method        = forms.CharField(label   = 'Method description',       required = True)
    results       = forms.FileField(label   = 'Results file (txt)',       required = True)
    miscellaneous = forms.FileField(label   = 'Miscellaneous file (zip)', required = False)

    def clean_results(self):
        results = self.cleaned_data['results']
        if not results.name.endswith('.txt'):
            raise forms.ValidationError("The results file must be in txt format")
        return results

    def clean_miscellaneous(self):
        miscellaneous = self.cleaned_data['miscellaneous']
        if miscellaneous:
            if not miscellaneous.name.endswith('.zip'):
                raise forms.ValidationError("The miscellaneous file must be in zip format")
            return miscellaneous


class filterform(forms.Form):

    application   = forms.CharField(label   = 'Application',              required = False)
    topology      = forms.CharField(label   = 'Topology',                 required = False)
    analysis      = forms.CharField(label   = 'Analysis',                 required = False)
    contact       = forms.CharField(label   = 'Contact',                  required = False)
    flexibility   = forms.CharField(label   = 'Flexibility',              required = False)

