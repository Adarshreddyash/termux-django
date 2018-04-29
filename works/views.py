from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from works.models import work

class workForm(ModelForm):
    class Meta:
        model = work
        fields = ['name', 'ip', 'order']

def work_list(request, template_name='/works/work_list.html'):
    works = work.objects.all()
    data = {}
    data['object_list'] = works
    return render(request, template_name, data)

def work_create(request, template_name='works/work_form.html'):
    form = workForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('work_list')
    return render(request, template_name, {'form':form})

def work_update(request, pk, template_name='works/work_form.html'):
    work = get_object_or_404(work, pk=pk)
    form = workForm(request.POST or None, instance=work)
    if form.is_valid():
        form.save()
        return redirect('work_list')
    return render(request, template_name, {'form':form})

def work_delete(request, pk, template_name='works/work_delete.html'):
    work = get_object_or_404(work, pk=pk)    
    if request.method=='POST':
        work.delete()
        return redirect('work_list')
    return render(request, template_name, {'object':work})