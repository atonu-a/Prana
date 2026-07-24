from django.db import models
from django.contrib.auth.models import User
from languages_plus.models import Language
class Profile(models.Model):
    GENDER = (
        ('Male', "Male"),
        ('Female', "Female"),
        ('Other', "Prefer not to say")
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    birthday = models.DateField()
    gender = models.CharField(choices=GENDER, max_length=10, default="Male")
    nationality = models.CharField(blank=True, null=True)
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
        related_name="users"
    )
    def __str__(self):
        return self.user.username
    


# Create your models here.
