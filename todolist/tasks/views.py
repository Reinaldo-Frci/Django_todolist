from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.
def lista_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('-data_criacao')
    return render(request, 'tasks/lista.html', {'tarefas': tarefas})

def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tasks/form.html', {'form': form})

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tasks/form.html', {'form': form})

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'tasks/confirma_exclusao.html', {'tarefa': tarefa})
