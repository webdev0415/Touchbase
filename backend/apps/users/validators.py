from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

class TouchbaseUsernameValidator(RegexValidator):
    # regex to only allow letters, numbers, and ./_ characters.
    regex = r'^[\w.]+$'
    message = _('Username may contain only letters, numbers, . or _')

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message= _("Phone number must be entered in the format: '+999999999'. Up to 15 digits.")
)