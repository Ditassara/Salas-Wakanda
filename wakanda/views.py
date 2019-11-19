# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Tipo, Sala, Arriendo

# Create your views here.
def index(request):
	return render(request,'index.html')
	
def salas(request):
	return render(request,'salas.html')

# class ArriendoCreate(CreateView):
# 	model = Arriendo
# 	fields = '__all__'
# 	initial = {'start_day',}

# class ArriendoUpdate(UpdateView):
# 	model = Arriendo
# 	fields = ['nombre','correo','fecha','sala','horas']

# class ArriendoDelete(DeleteView):
# 	model = Arriendo
# 	success_url = reverse_lazy('arriendo')

# from django.views import generic

# class ArriendoDetailView(generic.DetailView):
# 	model = Arriendo