from django import forms

class PostForm(forms.Form):
    project_title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Project Title"}))
    project_image = forms.ImageField()
    project_description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Project Description"}))
    project_url = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Link to live Site"}))

class design_rating(forms.Form):
    design_rating = forms.IntegerField()

class usability_rating(forms.Form):
    usability_rating = forms.IntegerField()

class content_rating(forms.Form):
    content_rating = forms.IntegerField()