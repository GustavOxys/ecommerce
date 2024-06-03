from django.template import Library
from utils import utils


register = Library()


@register.filter
def formate_price(value):
    return utils.formate_price(value)