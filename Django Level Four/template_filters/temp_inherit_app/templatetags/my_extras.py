from django import template


register = template.Library()

@register.filter(name='cut')        # ------------- Register custom filter WAY 1 (One of both ways)
def cut(value,arg):
    """
    This cuts all the values of "arg" from the string!
    """
    register value.replace(arg,'')


#   register.filter('cut',cut)      # ------------- Register custom filter WAY 2 (One of both ways)
