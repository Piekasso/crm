from django.forms import ModelForm
from django import forms

from .models import *


class Debitor_Form(ModelForm):
	class Meta:
		model = Debitor
		fields = '__all__'


class Kreditor_Form(ModelForm):
	class Meta:
		model = Kreditor
		fields = '__all__'


class Ausgangsrechnung_Form(ModelForm):
	class Meta:
		model = Ausgangsrechnung
		fields = '__all__'

class Eingangsrechnung_Form(ModelForm):
	class Meta:
		model = Eingangsrechnung
		fields = '__all__'
