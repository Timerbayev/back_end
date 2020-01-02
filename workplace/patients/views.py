from django.shortcuts import render
from .forms import PatientForm, Message
from django.http import HttpResponseRedirect


def patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clinic/')
    else:
        form = PatientForm()
    return render(request, 'patients/patient.html', {'form': form})


def check(request):
    if request.method == "POST":
        form = Message(request.POST)
    else:
        form = Message()
    return render(request, 'head_admin.html', locals())


def test(request, *args, **kwargs):
    print("OK")
    return HttpResponse('OK')