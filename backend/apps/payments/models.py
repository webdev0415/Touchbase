from django.db import models
from django.conf import settings
from apps.users.validators import phone_regex

class Transaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='transactions',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(verbose_name='Registered at', auto_now_add=True)
    fraud_status = models.CharField(max_length=15, default='none')
    modified = models.DateTimeField(auto_now=True)

    payment_status = models.CharField(max_length=15, default='waiting')
    payment_method = models.CharField(max_length=20, default='paypal')
    payment_id = models.CharField(max_length=150, default='', unique=True)
    payment_token = models.CharField(max_length=150, default='')
    payer_id = models.CharField(max_length=100, default='')
    payer_ipv4 = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)

    price_total = models.DecimalField(max_digits=9, decimal_places=2, default='0.0')
    
    # state/province/region
    billing_state = models.CharField(max_length=40, default='')
    billing_city = models.CharField(max_length=40, default='')
    billing_country = models.CharField(max_length=20, default='')
    billing_first_name = models.CharField(max_length=30, default='')
    billing_last_name = models.CharField(max_length=30, default='')
    billing_phone = models.CharField(validators=[phone_regex], max_length=17, default='', blank=True)
    billing_email = models.EmailField(verbose_name='Email', max_length=255)

    def __str__(self):
        return f"{self.payment_id}, on {self.created}"