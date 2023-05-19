from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from currency.models import Rate
from currency import constants


User = get_user_model()


@receiver(post_save, sender=Rate)
def rate_create_clear_cache(sender, instance, created, **kwargs):
    if created:
        cache.delete(constants.LATEST_RATE_CACHE)
