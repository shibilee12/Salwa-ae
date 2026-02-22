import os
from django.conf import settings
from django.http import FileResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import render
from .models import Item

BUSINESS_CONFIG = {
    'studio': {
        'template': 'business/studio.html',
        'background': 'images/bg_studio.jpg',
        'title': 'Salwa Studio'
    },
    'perfumes': {
        'template': 'business/perfumes.html',
        'background': 'images/bg_perfumes.jpg',
        'title': 'Salwa Perfumes'
    },
    'cafe': {
        'template': 'business/cafe.html',
        'background': 'images/bg_cafe.jpg',
        'title': 'Salwa Café'
    },
    'electricals': {
        'template': 'business/electricals.html',
        'background': 'images/bg_electricals.jpg',
        'title': 'Salwa Electricals'
    },
    'bookshop': {
        'template': 'business/bookshop.html',
        'background': 'images/bg_bookshop.jpg',
        'title': 'Salwa Bookshop'
    }
}

def home(request):
    return render(request, 'home2.html')

def business_page(request, business):
    config = BUSINESS_CONFIG.get(business)

    items = Item.objects.filter(business_type=business)

    return render(request, config['template'], {
        'items': items,
        'background': config['background'],
        'business_title': config['title']
    })

@xframe_options_exempt
def serve_cafe_menu(request):
    pdf_path = os.path.join(settings.BASE_DIR, 'templates', 'cafemenu.pdf')
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="cafemenu.pdf"'
    return response
