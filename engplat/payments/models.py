from django.db import models
from django.contrib.auth import get_user_model


class UserPayment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    payment_bool = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)
    # TODO: acrescentar item adquirido e período disponível


# @receiver(post_save, sender=User)
# def create_user_payment(sender, instance, created, **kwargs):
#     if created:
#         UserPayment.objects.create(user=instance)
