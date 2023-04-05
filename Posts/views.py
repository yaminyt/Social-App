from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Post_Form
from .models import Post_Model

# Create your views here.
def index(request):
    if request.method== "POST":
        form=Post_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect(form.errors.as_json())
       
    
    posts=Post_Model.objects.all().order_by("-created_at")[:20]
    return render(request,"home.html", {"posts":posts})


def delete(request,post_id):
        posts=Post_Model.objects.get(id=post_id)
        posts.delete()
        return HttpResponseRedirect("/")


def editpage(request,post_id):
    posts=Post_Model.objects.get(id=post_id)
    if request.method== "POST":
         form=Post_Form(request.POST, request.FILES, instance=posts)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect("/")
         else:
            return HttpResponseRedirect(form.errors.as_json())
            
            
        
    return render(request,"edit.html", {"posts":posts})


def like (request, post_id):
    posts=Post_Model.objects.get(id=post_id)
    new_value=posts.likes+1
    posts.likes=new_value
    posts.save()
    return HttpResponseRedirect("/")