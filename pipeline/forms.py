from django import forms

# from pagedown.widgets import PagedownWidget

from .models import Pipeline
from .choices import *


class PipelineForm(forms.ModelForm):
    # content = forms.CharField(widget=PagedownWidget(show_preview=False))
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputName',\
                                     'type': 'text',\
                                      'placeholder': 'Enter Pipename', "autofocus":True,}),
                                max_length=30,
                                required=True,
                                )
    longitude = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputLongitude',\
                                     'type': 'text',\
                                      'placeholder': 'Enter Pipename', "autofocus":True,}),
                                max_length=30,
                                required=True,
                               )
    latitude = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputLatitude',\
                                     'type': 'text',\
                                      'placeholder': 'Enter Pipename', "autofocus":True,}),
                                max_length=30,
                                required=True,
                                )

    # timestamp = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Pipeline
        fields = [
            "name",
            "longitude",
            "latitude",
            "image"
            # "is_damage",
            # "damage_grade",
            # "timestamp"
        ]

class PipelineUpdateForm(forms.ModelForm):
    # content = forms.CharField(widget=PagedownWidget(show_preview=False))
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-inline',\
                                     'type': 'text',\
                                      'placeholder': 'lokoja_pipeline'}),
                                max_length=30,
                                required=True,
                                )
    longitude = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-inline',\
                                     'type': 'text',\
                                      'placeholder': '-94.420307'}),
                                max_length=30,
                                required=True,
                               )
    latitude = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-inline',\
                                     'type': 'text',\
                                      'placeholder': '44.968046'}),
                                max_length=30,
                                required=True,
                                )
    is_damaged = forms.ChoiceField(choices = DAMAGE_STATUS_CHOICES, label="", initial='',
        widget=forms.RadioSelect(),
        required=True)
    damage_grade = forms.ChoiceField(choices = LEAK_GRADE, widget=forms.Select(
        {'class':'form-control form-control-line'}
        ), 
        required=True)
    class Meta:
        model = Pipeline
        fields = [
            "name",
            "longitude",
            "latitude",
            "image",
            "is_damaged",
            "damage_grade",
            # "timestamp"
        ]
