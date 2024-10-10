from django.shortcuts import render,redirect
from .models import Blog
from .forms import blog_form, RegsitrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request, "index.html")

def blog_list(request):
    blogs = Blog.objects.all().order_by("-created_at")
    return render(request,"blog_list.html",{'blogs':blogs})

@login_required
def create_blog(request):
    if(request.method=="POST"):
        form = blog_form(request.POST, request.FILES)
        if form.is_valid():
            blogs = form.save(commit=False)
            blogs.user = request.user
            blogs.save()
            return redirect('blog_list')
    else:
        form = blog_form()
    return render(request,"blog_submit_form.html",{'form':form})


@login_required
def blog_edit(request,blog_id):
    blogs = get_object_or_404(Blog,pk=blog_id, user=request.user)
    if request.method=="POST":
        form = blog_form(request.POST,request.FILES, instance=blogs)
        if form.is_valid():
            blogs = form.save(commit=False)
            blogs.user = request.user
            blogs.save()
            return redirect('blog_list')
    else:
        form = blog_form(instance=blogs)
    return render(request,"blog_submit_form.html",{'form':form,})


@login_required
def blog_delete(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id,user=request.user)
    if request.method=="POST":
        blog.delete()
        return redirect('blog_list')
    return render(request,"delete_blog.html",{'blog':blog})

def register(request):
    if request.method == "POST":
        form = RegsitrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('blog_list')
    else:
        form = RegsitrationForm()
    return render(request,"registration/register.html",{'form':form})

def blog_view(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,"blog_view.html",{"blog":blog})