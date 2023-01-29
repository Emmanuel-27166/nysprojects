from django.urls  import path
from .import  views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('', views.home, name="home" ),
    path('about_board_of_dirs/', views.about_board_of_dirs, name="about_board_of_dirs" ),
    path('about_impact/', views.about_impact, name="about_impact" ),
    path('about_sponsors/', views.about_sponsors, name="about_sponsors" ),
    path('background_info/', views.background_info, name="background_info" ),
    path('about_staff/', views.about_staff, name="about_staff" ),
    path('admission/', views.admission, name="admission" ),
    path('alumni/', views.alumni, name="alumni" ),
    path('contact_us/', views.contact_us, name="contact_us" ),
    path('department/', views.department, name="department" ),
    path('gallery/', views.gallery, name="gallery" ),
    path('news/', views.news, name="news" ),
    path('other_location/',views.other_location, name="other_location"),
    path('application/',views.application, name="application"),
    path('about_us/',views.about_us, name="about_us"),
    path('background/',views.background, name="background"),
    path('mission_vision/',views.mission_vision, name="mission_vision"),
    path('implementation/',views.implementation, name="implementation"),
    path('objectives/',views.objectives, name="objectives"),
    path('donations/',views.donations, name="donations"),
    
]

