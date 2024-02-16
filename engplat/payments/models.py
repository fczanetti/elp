from django.db import models
from django.contrib.auth import get_user_model
from ordered_model.models import OrderedModel
from django.urls import reverse


class UserPayment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)
    # TODO: acrescentar item adquirido e período disponível


# @receiver(post_save, sender=User)
# def create_user_payment(sender, instance, created, **kwargs):
#     if created:
#         UserPayment.objects.create(user=instance)


class Product(OrderedModel):
    prod_name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.CharField(max_length=240)
    num_avail_days = models.IntegerField(help_text='Informar número de dias de duração da assinatura.')
    available = models.BooleanField()
    stripe_id = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.prod_name

    def get_absolute_url(self):
        return reverse('payments:product_page', args=(self.slug,))
