from urllib.parse import quote
from django.conf import settings


def salwa_site_config(request):
    """Expose contact and social config to all templates."""
    whatsapp = getattr(settings, 'CONTACT_WHATSAPP_NUMBER', '').replace('+', '').replace(' ', '')
    default_msg = getattr(settings, 'CONTACT_WHATSAPP_DEFAULT_MSG', 'Hello, I would like to enquire.')
    whatsapp_url = f'https://wa.me/{whatsapp}?text={quote(default_msg)}' if whatsapp else ''
    whatsapp_base = f'https://wa.me/{whatsapp}' if whatsapp else ''
    location_url = getattr(settings, 'CONTACT_LOCATION_URL', '#')

    return {
        'salwa_whatsapp_number': getattr(settings, 'CONTACT_WHATSAPP_NUMBER', ''),
        'salwa_whatsapp_url': whatsapp_url,
        'salwa_whatsapp_base': whatsapp_base,
        'salwa_location_url': location_url,
        'salwa_instagram': getattr(settings, 'SOCIAL_INSTAGRAM', ''),
        'salwa_facebook': getattr(settings, 'SOCIAL_FACEBOOK', ''),
        'salwa_linkedin': getattr(settings, 'SOCIAL_LINKEDIN', ''),
    }
