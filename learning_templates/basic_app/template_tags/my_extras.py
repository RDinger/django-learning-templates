from django import template

register = template.Library()

# the value and arg will be from the context_dict
@register.filter(name='cut')
def cut(value, arg):

	"""
	This cuts out all values of arg from the str
	"""

	return value.replace(arg, '')

# register.filter('cut', cut)

