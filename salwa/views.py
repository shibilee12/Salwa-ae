import os
from urllib.parse import quote
from django.conf import settings
from django.http import FileResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import render
from .models import Item

# Placeholder branch data; replace with DB or settings when content is ready.
def _whatsapp_url(text):
    num = getattr(settings, 'CONTACT_WHATSAPP_NUMBER', '').replace('+', '').replace(' ', '')
    return f'https://wa.me/{num}?text={quote(text)}' if num else '#'

STUDIO_BRANCHES = [
    {'name': 'Branch 1', 'address': 'Address to be added.', 'enquiry_url': _whatsapp_url('Hi, I would like to enquire about Salwa Studio - Branch 1.')},
    {'name': 'Branch 2', 'address': 'Address to be added.', 'enquiry_url': _whatsapp_url('Hi, I would like to enquire about Salwa Studio - Branch 2.')},
    {'name': 'Branch 3', 'address': 'Address to be added.', 'enquiry_url': _whatsapp_url('Hi, I would like to enquire about Salwa Studio - Branch 3.')},
    {'name': 'Branch 4', 'address': 'Address to be added.', 'enquiry_url': _whatsapp_url('Hi, I would like to enquire about Salwa Studio - Branch 4.')},
]

BUSINESS_CONFIG = {
    'studio': {
        'template': 'business/studio.html',
        'background': 'images/bg_studio.jpg',
        'title': 'Salwa Studio',
        'theme': 'studio',
    },
    'perfumes': {
        'template': 'business/perfumes.html',
        'background': 'images/bg_perfumes.jpg',
        'title': 'Salwa Perfumes',
        'theme': 'perfumes',
    },
    'cafe': {
        'template': 'business/cafe.html',
        'background': 'images/bg_cafe.jpg',
        'title': 'Salwa Café',
        'theme': 'cafe',
    },
    'electricals': {
        'template': 'business/electricals.html',
        'background': 'images/bg_electricals.jpg',
        'title': 'Salwa Electricals',
        'theme': 'electricals',
    },
    'bookshop': {
        'template': 'business/bookshop.html',
        'background': 'images/bg_bookshop.jpg',
        'title': 'Salwa Bookshop',
        'theme': 'bookshop',
    }
}

def home(request):
    return render(request, 'home2.html')


def about(request):
    return render(request, 'about.html')


def careers(request):
    return render(request, 'careers.html')


def contact(request):
    return render(request, 'contact.html')

def business_page(request, business):
    config = BUSINESS_CONFIG.get(business)
    if not config:
        from django.http import Http404
        raise Http404('Division not found')

    items = Item.objects.filter(business_type=business)
    context = {
        'items': items,
        'background': config['background'],
        'business_title': config['title'],
        'business_slug': business,
        'theme': config.get('theme', business),
    }
    if business == 'studio':
        context['studio_branches'] = STUDIO_BRANCHES
    return render(request, config['template'], context)

@xframe_options_exempt
def serve_cafe_menu(request):
    from django.http import Http404
    pdf_path = os.path.join(settings.BASE_DIR, 'templates', 'cafemenu.pdf')
    if not os.path.isfile(pdf_path):
        raise Http404('Menu not found')
    with open(pdf_path, 'rb') as f:
        response = FileResponse(f, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="cafemenu.pdf"'
    return response
