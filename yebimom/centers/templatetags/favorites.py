from django import template


register = template.Library()


@register.filter(name='favorite_class')
def favorite_class(user, center):
    if _is_center_in_favorites(user, center):
        return "favorite-on"
    else:
        return "favorite-off"


def _is_center_in_favorites(user, center):
    return user.userprofile.favorites.filter(id=center.id).exists()
