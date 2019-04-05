from django.urls import path
from . import views

urlpatterns = [
	path('',views.landing, name='landing-page'),
	path('profile/',views.visvalize, name='visvalize'),
	path('data-entry/',views.getdata, name='getdata'),
	path('profile/floor/<int:offset>/',views.insidefloor, name='inside_floor'),
	path('profile/floor/<int:offset>/<slug:slug>/',views.sensor, name='sensor'),

]