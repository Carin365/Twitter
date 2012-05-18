from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Auth(models.Model):
    image = models.ImageField(upload_to="img")
    name = models.CharField(max_length=25)
    born_date = models.DateField()
    location = models.CharField(max_length=25)
    tweets = models.CharField(max_length=140)

    #user = models.OneToOneField('auth.User')


class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.TextField(max_length=150)
    userr = models.ForeignKey(User)

class Follow(models.Model):
    fecha = models.DateTimeField()
    activo = models.BooleanField()
    follower = models.ForeignKey('Users')
    followed = models.ForeignKey(User)

class Users(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField(null=True)
    image = models.ImageField(upload_to="img", null=True)
    location = models.CharField(max_length=25, null=True)
    name = models.CharField(max_length=30, null=True)
    about_me = models.TextField(max_length=150, null=True)

    def __unicode__(self):
        return '%s' % self.name

def get_profile(user):
    if not hasattr(user, '_profile_cache'):
        profile, created = Users.objects.get_or_create(user=user)
        user._profile_cache = profile
    return user._profile_cache
User.get_profile = get_profile


#def create_user(sender, instance, **kwargs):
#    users, new = User.objects.get_or_create(user=instance)
#post_save.connect(create_user, User)