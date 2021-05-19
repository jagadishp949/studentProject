from django import forms
from django.core import validators
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe

import pandas as pd
alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only characters are allowed.')
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
class StudentForm(forms.Form):
    Name = forms.CharField(max_length=40, validators=[alpha])
    RollNumber = forms.CharField(max_length=15, validators=[alphanumeric])
    Age = forms.IntegerField(min_value=1)
    # GENDER_CHOICES = (('M', 'Male'),
    #     ('F', 'Female'),)
    CHOICES = [('M', 'Male'), ('F', 'Female')]
    # #gender = forms.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    # Gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))
    Gender=forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,
					)


  #  Name.widget.attrs.update({'class': 'form-group col-md-6'})

    #Gender.widget.attrs.update({'class': 'form-check form-check-inline'})

def clean(self):
	print("validation data")
	total_cleaned_data=super().clean()
	df = pd.read_csv("student.csv")

	found=False
	if df.empty:
		print("empty data")
	else:
		for ind in df.index:
			if df['RollNumber'][ind] ==int(total_cleaned_data['RollNumber']):
				found=True
				break;
	if found:
		#raise ValidationError('please check Roll Number, A student is registed with the following Roll Number')
			raise forms.ValidationError("You have forgotten about Fred!")
	
