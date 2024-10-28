from django import forms
from .models import Project


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de Tarea", max_length=200, widget=forms.TextInput(attrs={'class':"input"}))
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class':"input"}))
    
    project = forms.ModelChoiceField(label="Proyecto", queryset=Project.objects.all())


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Projecto", max_length=200, widget=forms.TextInput(attrs={'class':"input"}))
