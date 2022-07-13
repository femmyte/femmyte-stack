from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import SlugField
# we use AbstractUser model anytime we want to create our own usert model

from .managers import CustomUserManager
from django.template.defaultfilters import slugify
from . import utils


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    # we didnt want username
    # we use email as the unique field

    # this will provide username by default is the user left it blank
    slug = models.SlugField(blank=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['email']
        verbose_name = 'User'
        # this is what will show in the user admin from CustomUser to User model

    def __str__(self):
        return self.email

    # creating a default slug/username for users if blank

    def gen_random_slug(self):
        # we generate a username with the users firstname and lastname bu in order to avoid the same username we append a random number to the name
        random_slug = slugify(
            self.first_name + self.last_name + utils.generate_random_id())
        # if the user's firstname and lastname are the same and also the random number we
        # loop through untill we get different random number
        while CustomUser.objects.filter(slug=random_slug).exists():
            random_slug = slugify(
                self.first_name + self.last_name + utils.generate_random_id())
        return random_slug

    def save(self, *args, **kwargs):
        # check for a slug
        if not self.slug:
            # create default slug
            self.slug = self.gen_random_slug()

        #  save
        super().save(*args, **kwargs)
