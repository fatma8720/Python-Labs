from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Prof

def prof_list(request):
    profs = Prof.objects.all()
    return render(request, 'prof/list.html', context={'profs': profs})

def prof_details(request, name):
    prof = Prof.objects.filter(name=name).first()
    return render(request, 'prof/details.html', context={'prof': prof})

def prof_add(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        department = request.POST.get('department')
        rank = request.POST.get('rank')
        if name and department and rank:
            Prof.objects.create(name=name, department=department, rank=rank)
            return redirect(Prof.get_list_url())
        else:
            context['msg'] = 'Please provide name, department, and rank'
    return render(request, 'prof/add.html', context)

def prof_update(request, id):
    prof = Prof.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        department = request.POST.get('department')
        rank = request.POST.get('rank')
        if name and department and rank:
            prof.name = name
            prof.department = department
            prof.rank = rank
            prof.save()
            return redirect(Prof.get_list_url())
    return render(request, 'prof/update.html', context={'prof': prof})

def prof_delete(request, id):
    prof = Prof.objects.filter(id=id).delete()
    return redirect('prof_list')
