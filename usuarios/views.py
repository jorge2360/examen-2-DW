from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Usuario
from .forms import UsuarioForm

class UsuariosListCreateView(ListView, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios.html'
    success_url = '/usuarios/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios'] = Usuario.objects.all()
        context['form'] = UsuarioForm()
        return context

    def post(self, request, *args, **kwargs):
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        return render(request, 'usuarios.html', {'form': form})