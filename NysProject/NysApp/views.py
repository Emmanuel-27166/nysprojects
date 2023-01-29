from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# ===========demo =============
def demo(request):
    return render(request, 'pages/demo.html')
    # return HttpResponse("hillllll")

# ===========home =============
def home(request):
    return render(request, 'pages/home.html')

     

# ===========about =============
def background_info(request):
    return render(request, 'pages/about_pages/background_info.html')
    
def about_staff(request):
    return render(request, 'pages/about_pages/about_staff.html')
    
def about_board_of_dirs(request):
    return render(request, 'pages/about_pages/about_board_of_dirs.html')

def about_impact(request):
    return render(request, 'pages/about_pages/about_impact.html')

def about_sponsors(request):
    return render(request, 'pages/about_pages/about_sponsors.html')

# ========news=================
def news(request):
    return render(request, 'pages/news.html')

# ==========department================
def department(request):
    return render(request, 'pages/department.html')

# =============gallery================

def gallery(request):
    return render(request, 'pages/gallery.html')

# =============contact us=================
def contact_us(request):
    return render(request, 'pages/contact_us.html')

# =============Alumni=================
def alumni(request):
    return render(request, 'pages/alumni.html')

# =============admission===============
def admission(request):
    return render(request, 'pages/admission.html')

# =============SUB_PAGES SECTION-=============
def other_location(request):
    return render(request, "pages/sub_pages/other_location.html")

def application(request):
    return render(request, "pages/sub_pages/application.html")

def about_us(request):
    return render(request, "pages/about_pages/about_us.html")

def background(request):
    return render(request, "pages/about_pages/background.html")

def implementation(request):
    return render(request, "pages/about_pages/implementation.html")

def objectives(request):
    return render(request, "pages/about_pages/objectives.html")

def mission_vision(request):
    return render(request, "pages/about_pages/mission_vision.html")

def donations(request):
    return render(request, "pages/sub_pages/donations.html")





