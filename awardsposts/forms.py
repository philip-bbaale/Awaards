from django import forms

class PostForm(forms.Form):
    project_title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Project Title"}))
    project_image = forms.ImageField(widget=forms.ImageField(attrs={"class": "form-control","placeholder": "Project Image"}))
    project_description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Project Description"}))
    project_url = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Link to live Site"}))