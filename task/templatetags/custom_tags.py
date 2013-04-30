from django.core.urlresolvers import reverse
from django import template

register = template.Library()

@register.simple_tag(name = 'url_to_edit_object')
def url_to_edit_object(object):
  url = reverse('admin:%s_%s_change' %(object._meta.app_label,  object._meta.module_name),  args=[object.id] )
  return u'<a href="%s">[Edit %s]</a>' %(url,  object.__unicode__())