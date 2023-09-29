from django import template

from ..models import BaseNavigationSnippet
from wagtail.models import Locale
# from wagtail_localize.query import LocalizedQuerySet

register = template.Library()

@register.simple_tag()
def get_navigation_menu(slug):
    active_locale = Locale.get_active().language_code
    locale = Locale.objects.get(language_code=active_locale)
    snippet = BaseNavigationSnippet.objects.filter(locale=locale, slug=slug).first()
    
    if active_locale != 'en' and snippet is None:
        english = Locale.objects.get(language_code='en')
        return BaseNavigationSnippet.objects.filter(locale=english, slug=slug).first()
    
    return snippet
