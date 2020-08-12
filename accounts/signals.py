from django.db.models.signals import post_save
from django.contrib.auth.models import Group, User
from .models import Customer


def create_profile(sender, instance, created, **kwargs):

    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username
        )
        print('Profile has been created!')

post_save.connect(create_profile, sender=User)