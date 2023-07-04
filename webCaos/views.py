from django.views.generic import ListView
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login as login_aut
from .carrito import *
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


class SearchNoticias(ListView):
    model = Noticia
    template_name = 'galeria.html'
    context_object_name = 'noticias'

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Noticia.objects.filter(titulo__icontains=query).order_by('fecha')

def cerrar_sesion(request):
    logout(request)
    categorias = Categoria.objects.all()
    noticias = Noticia.objects.filter(publicar= True).order_by("-idNoticia")[:4]
    print(noticias)
    contexto={'categorias':categorias,'noticias':noticias}

    return render(request,'index.html', contexto)

def login(request):
    if request.POST:
        mail=request.POST.get("txtEmail")
        con=request.POST.get("pwdPass1")
        print(mail)
        print(con)
        usu= authenticate(request,username=mail,password=con)
        if usu is not None and usu.is_active:
            login_aut(request,usu)
            categorias = Categoria.objects.all()
            noticias = Noticia.objects.filter(publicar = True).order_by("-idNoticia")[:4]
            print(noticias)
            contexto={'categorias':categorias,'noticias':noticias}

            return render(request,"index.html", contexto)
    contexto={'mensaje':'Usuario/Contraseña Incorrecto'}   
    return render(request,"inicio_sesion.html",contexto)

def index(request):
    categorias = Categoria.objects.all()
    noticias = Noticia.objects.filter(publicar = True).order_by("-idNoticia")[:4]
    print(noticias)
    contexto={'categorias':categorias,'noticias':noticias}

    return render(request,'index.html', contexto)



def galeria(request):
    noticias = Noticia.objects.filter(publicar = True)
    categorias = Categoria.objects.all()
    data = {"noticias": noticias, "categorias": categorias}
    if request.POST:
        nom = request.POST.get("txtBuscar")
        noticias = Noticia.objects.filter(titulo = nom)
        categorias = Categoria.objects.all()
        print(Noticia)


    return render(request,'galeria.html', data)

def inicio_sesion(request):
    return render(request, 'inicio_sesion.html')

def deportes(request):
    noticias = Noticia.objects.filter(publicar = True)
    categorias = Categoria.objects.all()
    data = {"noticias": noticias, "categorias": categorias}
    print(noticias)
    return render(request, 'deportes.html', data)

def formulario(request):
    contexto={'mensaje':''}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        rut = request.POST.get("txtRut")
        email= request.POST.get("txtEmail")
        password= request.POST.get("pwdPass1")
        usu = User()
        usu.set_password(password)
        usu.rut=rut
        usu.email=email
        usu.username=nombre
        usu.last_name=apellido
        usu.first_name=nombre
        try:
            usu.save()
            contexto['mensaje']='Usuario Registrado'    
        except:
            contexto['mensaje']='error al registrar usuario' 
    return render(request, 'formulario.html', contexto)

def internacional(request):
    noticias = Noticia.objects.filter(publicar = True)
    categorias = Categoria.objects.all()
    data = {"noticias": noticias, "categorias": categorias}
    print(noticias)
    return render(request, 'internacional.html', data)

def nacional(request):
    noticias = Noticia.objects.filter(publicar = True)
    categorias = Categoria.objects.all()
    data = {"noticias": noticias, "categorias": categorias}
    print(noticias)
    return render(request, 'nacional.html', data)

def politica(request):
    noticias = Noticia.objects.filter(publicar = True)
    categorias = Categoria.objects.all()
    data = {"noticias": noticias, "categorias": categorias}
    print(noticias)
    return render(request, 'politica.html', data)

@login_required(login_url='login/')
def perfil_periodista(request):
    return render(request, 'perfil_periodista.html')

@login_required(login_url='login/')
@permission_required(['webCaos.add_noticia','webCaos.change_noticia','webCaos.delete_noticia'], login_url='login/')
def noticias(request):
    noticias = Noticia.objects.all()
    categorias = Categoria.objects.all()
    data = {"noticias": noticias, "categorias": categorias}
    return render(request, 'noticias.html', data)


def carrito(request):
    return render(request, 'carrito.html')

@login_required(login_url='login/')
@permission_required(['webCaos.add_noticia'], login_url='login/')
def ingresar_noticia(request):
    categorias= Categoria.objects.all()
    contexto={'categorias':categorias}
    if request.POST:
        titulo = request.POST.get("txtTitulo")
        desc =request.POST.get("txtDescripcion")
        fec = request.POST.get("datFecha")
        foto = request.FILES.get("txtImg")
        print(foto)
        cate = request.POST.get("cboCategoria")
        obj_cate = Categoria.objects.get(nombre=cate)
        noti = Noticia(
            titulo=titulo,
            fecha= fec,
            descripcion= desc,
            foto=foto,
            categoria=obj_cate,
        )
        noti.save()
        contexto["mensaje"]="Grabo"
        return render(request,"ingresar_noticia.html",contexto)

    return render(request,"ingresar_noticia.html",contexto)

def productos(request):
    produ = producto.objects.all()
    data = {"produ": produ}
    return render(request, 'productos.html', data)



def agregar_carrito(request, id_producto):
    carrito = Carrito(request)
    produ = producto.objects.get(idProducto = id_producto)
    carrito.agregar(produ)
    return redirect('PROD')

def restar_carrito(request, id_producto):
    carrito = Carrito(request)
    produ = producto.objects.get(idProducto = id_producto)
    carrito.restar(produ)
    return redirect('PROD')

def eliminar_carrito(request, id_producto):
    carrito = Carrito(request)
    produ = producto.objects.get(idProducto = id_producto)
    carrito.eliminar(produ)
    return redirect('PROD')

def vaciar(request):
    carrito = Carrito(request)
    carrito.vaciar()
    return redirect('PROD')

@login_required(login_url='login/')
@permission_required(['webCaos.delete_noticia'], login_url='login/')
def eliminar_noticia(request, id):
    noticia = Noticia.objects.get(idNoticia = id)
    noticias = Noticia.objects.all()
    categorias = Categoria.objects.all()
    data = {"noticias": noticias, "categorias": categorias}
    data ['mensaje']=''
    try:
        noticia.delete()
        data["mensaje"] = 'no eliminó'
    except:
        data["mensaje"] = 'no eliminó'
    return render(request, 'noticias.html', data)

@login_required(login_url='login/')
@permission_required(['webCaos.change_noticia'], login_url='login/')
def modificar(request, id):
    noticia = Noticia.objects.get(idNoticia = id)
    categorias = Categoria.objects.all()
    data = {'noticia': noticia, 'categorias':categorias}
    return render(request, "editar_noticia.html", data)

@login_required(login_url='login/')
@permission_required(['webCaos.change_noticia'], login_url='login/')
def editar_noticia(request):
    if request.POST:
        id = request.POST.get("txtId")
        titulo = request.POST.get("txtTitulo")
        desc =request.POST.get("txtDescripcion")
        fec = request.POST.get("datFecha")
        foto = request.FILES.get("txtImg")
        print(foto)
        cate = request.POST.get("cboCategoria")
        obj_cate = Categoria.objects.get(nombre=cate)
        noti = Noticia.objects.get(idNoticia = id)
        noti.titulo = titulo
        titulo=titulo
        noti.descripcion= desc
        noti.fecha= fec
        if foto is not None:
            foto=foto    
        noti.categoria=obj_cate
        noti.save()
    return redirect('noticias/')

@login_required(login_url='login/')
def agregar_imagen(request):
    if request.POST:
        id = request.POST.get("txtId")
        foto = request.FILES.get("txtFoto")
        noticia = Noticia.objects.get(idNoticia = id)
        gale = Galeria(
            foto = foto,
            noticia = noticia
        )
        gale.save()
    return redirect("noticias/")



def galeria_noti(request, id):
    noticia = Noticia.objects.get(idNoticia = id)
    galeria = Galeria.objects.filter(noticia = noticia)
    data = {'noticia': noticia, 'galeria': galeria}
    return render(request, "galeria_noti.html", data)
         