from django import template


register = template.Library()


@register.filter(name='group_by')
def group_by(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i + n]
