from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from .formularios.registerform import NewUserForm
from .formularios.loginform import LoginForm
from .formularios.add_prov import Add_prove
from .formularios.add_produc import Add_produ
from .models import Productos,Proveedores

def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect("/")
    else:
        formulario = NewUserForm()
        return render(request,"Reg_user.html",{"form":formulario})

@login_required(login_url='login')
def index(request): 
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()
    es_admin = request.user.is_staff
    if es_estudiante or es_admin:
        return render(request, 'index.html', {'user':
request.user, 'es_estudiante': es_estudiante,'es_admin': es_admin})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def index(request):
 return render(request, 'index.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

# Lista de Proveedores
def list_prov(request):
    proveedores = Proveedores.objects.all()
    return render(request,"lisprov.html",{"lisprov": proveedores})

def es_admin(user):
    return  user.is_staff

#Añadir Proveedores
@user_passes_test(es_admin, login_url='login')
def add_proveedor(request):
    if request.method == "POST":
        fm = Add_prove(request.POST)
        if fm.is_valid():
            nuevoreg = Proveedores()
            nuevoreg.nombre = fm.data["nombre"]
            nuevoreg.telefono = fm.data["telefono"]
            nuevoreg.save()
            return HttpResponseRedirect("/")
    else:
        fm = Add_prove()
        return render(request,"Add_prov.html",{"fm":fm})
    
def add_producto(request):
    if request.method =="POST":
        formu = Add_produ(request.POST)
        if formu.is_valid():
            nuevoreg = Productos()
            nuevoreg.nombre = formu.data["nombre"]
            nuevoreg.stock = formu.data["stonk"]
            nuevoreg.save()
            return HttpResponseRedirect("/")
    else:
        formu = Add_produ()
        return render(request,"Add_produc.html",{"fmro":formu})

def list_prod(request):
    productos = Proveedores.objects.all()
    return render(request,"lisprod.html",{"lisprodu": productos})