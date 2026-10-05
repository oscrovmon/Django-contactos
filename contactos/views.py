from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Contacto, Provincia
from .forms import ContactoForm

def inicio(request):
    query = request.GET.get('q', '')
    provincia_id = request.GET.get('provincia', '')

    contactos = Contacto.objects.all()

    if query:
        contactos = contactos.filter(
            Q(nombre__icontains=query) | 
            Q(email__icontains=query) | 
            Q(telefono__icontains=query)
        )

    if provincia_id:
        contactos = contactos.filter(provincia_id=provincia_id)

    provincias = Provincia.objects.all()

    return render(request, 'contactos/index.html', {
        'contactos': contactos,
        'provincias': provincias,
        'query': query,
        'provincia_seleccionada': provincia_id
    })

def ficha(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'contactos/ficha.html', {'contacto': contacto})

@login_required
def nuevo(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ContactoForm()
    return render(request, 'contactos/formulario.html', {'form': form, 'titulo': 'Nuevo Contacto'})

@login_required
def editar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, request.FILES, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('ficha', pk=contacto.pk)
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contactos/formulario.html', {'form': form, 'titulo': 'Editar Contacto'})

@login_required
def eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('inicio')
    return render(request, 'contactos/confirmar_eliminar.html', {'contacto': contacto})
