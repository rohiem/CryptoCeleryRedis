# Suggested code may be subject to a license. Learn more: ~LicenseLog:873963853.
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Test
from .tasks import create_code

@receiver(post_save,sender=Test)
def set_codes(sender,instance,created,*args,**kwargs):
    if created:
        create_code.delay()
    else:
        create_code.delay()