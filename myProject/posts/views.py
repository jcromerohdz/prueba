from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required


from .forms import PostForm
from .models import Post

# Create your views here.

def post_home(request):
	#query = Post.objects.all()
	saludo = "Hola"
	print "hola mundo!"
	context = {
			"saludo":saludo,	
		}
	return render(request,"base_2.html", context)

@login_required
def crear_post(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.save()
		messages.success(request, 'Fue creado exitosamente!.')
		return HttpResponseRedirect("/contenido/")
	#if request,method = "POST":
		#print request.POST.get("titulo")
	#else:
		#messages.error(request, "No fue creado exitosamente!")
	
	context = {
			"form":form,	
		}
	return render(request,"forma_post.html", context)

@login_required
def actualizar_post(request,id=None):
	query = get_object_or_404(Post, pk=id)
	form = PostForm(request.POST or None, request.FILES or None, instance = query)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect("/contenido/")
	context = {
			"detalle":query,
			"form":form,	
		}
	return render(request,"forma_post.html", context)

@login_required
def borrar_post(request, id=id):
	query = get_object_or_404(Post, pk=id)
	query.delete()
	messages.success(request, 'Fue eliminado exitosamente!.')
	return redirect("/contenido/")


@login_required
def detalle_post(request,id=None):
	query = get_object_or_404(Post, pk=id)	
	context = {
			"detalle":query,	
		}
	return render(request,"detalle.html", context)

@login_required
def contenido_post(request):
	query_list = Post.objects.all().order_by("-creado")
	paginator = Paginator(query_list, 5) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
	    query = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    query = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    query = paginator.page(paginator.num_pages)
	saludo = "Contenido"
	print "hola mundo!"
	context = {
			"listado_objetos":query,
			"saludo":saludo,	
		}
	return render(request,"contenido.html", context)
