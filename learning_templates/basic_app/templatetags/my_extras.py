from django import template

register = template.Library()

def cut(value,arg):
    """
    THIS CUTS ALL THE VALUES OF ARG FROM THE STRING
    """
    return value.replace(arg,'')

register.filter('cut',cut)
