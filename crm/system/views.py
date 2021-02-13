from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import AusgangsrechnungFilter, EingangsrechnungFilter

def index(request):

    context = {'title':'Startseite'}
    return render(request, 'system/index.html', context)

################################################################
#Debitoren
################################################################

def alle_debitoren(request):

    debitoren = Debitor.objects.all().order_by('-id')
    context = {'alle_debitoren':debitoren, 'title':'Debitoren'}
    return render(request, 'system/alle_debitoren.html', context)


def neuer_debitor(request):

    debitor_form = Debitor_Form()
    if request.method == 'POST':
        debitor_form = Debitor_Form(request.POST)
        if debitor_form.is_valid():
            debitor_form.save()
            return redirect('alle_debitoren')
    context = {'debitor_form':debitor_form, 'title':'Neuer Debitor'}
    return render(request, 'system/neuer_debitor.html', context)


def bearbeiten_debitor(request, pk):

    debitor = Debitor.objects.get(id=pk)
    debitor_form = Debitor_Form(instance=debitor)
    if request.method == 'POST':
        debitor_form = Debitor_Form(request.POST, instance=debitor)
        if debitor_form.is_valid():
            debitor_form.save()
            return redirect('alle_debitoren')
    context = {'debitor_form':debitor_form, 'title':'Debitor bearbeiten'}
    return render(request, 'system/neuer_debitor.html', context)

################################################################
#Kreditoren
################################################################

def alle_kreditoren(request):

    kreditoren = Kreditor.objects.all().order_by('-id')
    context = {'alle_kreditoren':kreditoren, 'title':'Kreditoren'}
    return render(request, 'system/alle_kreditoren.html', context)


def neuer_kreditor(request):

    kreditor_form = Kreditor_Form()
    if request.method == 'POST':
        kreditor_form = Kreditor_Form(request.POST)
        if kreditor_form.is_valid():
            kreditor_form.save()
            return redirect('alle_kreditoren')
    context = {'kreditor_form':kreditor_form, 'title':'Neuer Kreditor'}
    return render(request, 'system/neuer_kreditor.html', context)


def bearbeiten_kreditor(request, pk):

    kreditor = Kreditor.objects.get(id=pk)
    kreditor_form = Kreditor_Form(instance=kreditor)
    if request.method == 'POST':
        kreditor_form = Kreditor_Form(request.POST, instance=kreditor)
        if kreditor_form.is_valid():
            kreditor_form.save()
            return redirect('alle_kreditoren')
    context = {'kreditor_form':kreditor_form, 'title':'Kreditor bearbeiten'}
    return render(request, 'system/neuer_kreditor.html', context)

################################################################
#Ausgangsrechnungen
################################################################

def alle_ausgangsrechnungen(request):

    ausgangsrechnungen = Ausgangsrechnung.objects.all().order_by('-id')

    myFilter = AusgangsrechnungFilter(request.GET, queryset=ausgangsrechnungen)
    ausgangsrechnungen = myFilter.qs

    context = {'ausgangsrechnungen':ausgangsrechnungen, 'myFilter':myFilter, 'title':'Ausgangsrechnungen'}
    return render(request, 'system/alle_ausgangsrechnungen.html', context)


def neue_ausgangsrechnung(request):

    ausgangsrechnung_form = Ausgangsrechnung_Form()
    if request.method == 'POST':
        ausgangrechnung_form = Ausgangrechnung_Form(request.POST)
        if ausgangrechnung_form.is_valid():
            ausgangsrechnung_form.save()
            return redirect('alle_ausgangsrechnungen')

    context = {'ausgangsrechnung_form':ausgangsrechnung_form, 'title':'Neue Ausgangsrechnung'}
    return render(request, 'system/neue_ausgangsrechnung.html', context)



def debitor_ausgangsrechnung(request, id):

    ausgangsrechnungen = Ausgangsrechnung.objects.filter(debitor=id).order_by('-id')
    name = Debitor.objects.get(id=id)
    context = {'ausgangsrechnungen':ausgangsrechnungen, 'name':name, 'id':id, 'title':'Ausgangsrechnungen'}
    return render(request, 'system/ausgangsrechnungen.html', context)


def debitor_neue_ausgangsrechnung(request, debitor):

    ausgangsrechnung_form = Ausgangsrechnung_Form(initial={'debitor':debitor})
    if request.method == 'POST':
        ausgangsrechnung_form = Ausgangsrechnung_Form(request.POST, initial={'debitor':debitor})
        if ausgangsrechnung_form.is_valid():
            ausgangsrechnung_form.save()
            return redirect('alle_ausgangsrechnungen')

    context = {'ausgangsrechnung_form':ausgangsrechnung_form, 'title':'Neue Ausgangsrechnung'}
    return render(request, 'system/neue_ausgangsrechnung.html', context)


################################################################
#Eingangsrechnungen
################################################################

def alle_eingangsrechnungen(request):

    eingangsrechnungen = Eingangsrechnung.objects.all().order_by('-id')

    myFilter = EingangsrechnungFilter(request.GET, queryset=eingangsrechnungen)
    eingangsrechnungen = myFilter.qs

    context = {'eingangsrechnungen':eingangsrechnungen, 'myFilter':myFilter, 'title':'Eingangsrechnungen'}
    return render(request, 'system/alle_eingangsrechnungen.html', context)


def neue_eingangsrechnung(request):

    eingangsrechnung_form = Eingangsrechnung_Form()
    if request.method == 'POST':
        eingangrechnung_form = Eingangrechnung_Form(request.POST)
        if eingangrechnung_form.is_valid():
            eingangsrechnung_form.save()
            return redirect('alle_eingangsrechnungen')

    context = {'eingangsrechnung_form':eingangsrechnung_form, 'title':'Neue Eingangsrechnung'}
    return render(request, 'system/neue_eingangsrechnung.html', context)



def kreditor_eingangsrechnung(request, id):

    eingangsrechnungen = Eingangsrechnung.objects.filter(kreditor=id).order_by('-id')
    name = Kreditor.objects.get(id=id)
    context = {'eingangsrechnungen':eingangsrechnungen, 'name':name, 'id':id, 'title':'Eingangsrechnungen'}
    return render(request, 'system/eingangsrechnungen.html', context)


def kreditor_neue_eingangsrechnung(request, kreditor):

    eingangsrechnung_form = Eingangsrechnung_Form(initial={'kreditor':kreditor})
    if request.method == 'POST':
        eingangsrechnung_form = Ausgangsrechnung_Form(request.POST, initial={'kreditor':kreditor})
        if eingangsrechnung_form.is_valid():
            eingangsrechnung_form.save()
            return redirect('alle_eingangsrechnungen')

    context = {'eingangsrechnung_form':eingangsrechnung_form, 'title':'Neue Eingangsrechnung'}
    return render(request, 'system/neue_eingangsrechnung.html', context)
