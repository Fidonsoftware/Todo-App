from django import forms
from django.forms import ModelForm

from .models import *

class WorkForm(forms.ModelForm):

      class Meta:
          model = Work
          fields = '__all__'