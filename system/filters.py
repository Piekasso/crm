import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class AusgangsrechnungFilter(django_filters.FilterSet):

	class Meta:
		model = Ausgangsrechnung
		fields = '__all__'

class EingangsrechnungFilter(django_filters.FilterSet):

	class Meta:
		model = Eingangsrechnung
		fields = '__all__'
