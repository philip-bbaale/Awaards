from django import forms

class PostForm(forms.Form):
    project_title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Project Title"}))
    project_image = forms.ImageField()
    project_description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Project Description"}))
    project_url = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Link to live Site"}))

class RatingForm(forms.Form):
    design_rating = forms.IntegerField()
    usability_rating = forms.IntegerField()
    content_rating = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Leave a comment"}))

    