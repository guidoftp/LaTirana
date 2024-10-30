from django.shortcuts import render, redirect
from Aplicacion.forms import FormLibro
from Aplicacion.models import Libro

# Create your views here.

def index(request):
    return render(request, 'Aplicacion/index.html')

def listadoLibros(request):
    libros = Libro.objects.all()
    data = {'libros': libros} 
    return render(request, 'Aplicacion/libros.html', data)  # Asegúrate de que la plantilla sea "libros.html"

def agregarLibro(request):
    form = FormLibro()
    if request.method == 'POST':
        form = FormLibro(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')  # Redirige en lugar de renderizar directamente la vista
    data = {'form': form}   
    return render(request, 'Aplicacion/agregarLibro.html', data)

def eliminarLibro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('/libros/') 

def actualizarLibro(request, id):
    libro = Libro.objects.get(id=id)
    form = FormLibro(instance=libro)
    if request.method == 'POST':
        form = FormLibro(request.POST, instance=libro)
        if form.is_valid():
            form.save()
        return redirect('/')  # Redirige en lugar de renderizar directamente la vista
    data = {'form': form}
    return render(request, 'Aplicacion/agregarLibro.html', data)

