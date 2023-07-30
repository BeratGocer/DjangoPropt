from django import template
from blog.models import kategoriModel

register = template.Library()

@register.simple_tag
def kategoriList():
    kategoriler = kategoriModel.objects.all()
    return kategoriler
