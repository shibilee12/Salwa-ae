from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('careers/', views.careers, name='careers'),
    path('contact/', views.contact, name='contact'),
    path('business/<str:business>/', views.business_page, name='business'),
    path('cafe-menu.pdf', views.serve_cafe_menu, name='cafe_menu_pdf'),
]