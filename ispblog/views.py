
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .forms import CreateBlogForm,create_applied_for_view 
from .models import services , c_request, suport

# Create your views here.

def isp_home (request):
    isp_data = services.objects.all()
    context  = {'data':isp_data}

    return render (request, 'index.html',context) 


def C_Request (request):
    if request.method == "POST":
        # print("POST", request.POST)
        c_request.objects.create (
            Date = request.POST.get("Date"),
            package = request.POST.get("package"),
            phone  = request.POST.get("phone"),
            address = request.POST.get("address"),
            
        )
        return HttpResponseRedirect("/")
        # form = CreateBlogForm(request.POST)
    form = CreateBlogForm()
    return render (request, 'request.html', {"form": form})


def suport_request (request):
    if request.method == "POST":
        # print("POST", request.POST)
        suport.objects.create (
            question = request.POST.get("Date"),
            active_package = request.POST.get("package"),
            phone  = request.POST.get("phone"),
            address = request.POST.get("address"),
            
        )
        return HttpResponseRedirect("/")
        # form = CreateBlogForm(request.POST)
    form = create_applied_for_view()
    return render (request, 'support.html', {"form": form})

def package_view(request):
        # isp_data = services.objects.all()
        # context  = {'data':isp_data}

    return render (request, 'package.html' ) 