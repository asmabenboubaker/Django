from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
def only_int(value): 
    if value.isdigit()==False:
        raise ValidationError("cin contains characters")
# Create your models here.
class Person(AbstractUser):
    cin = models.CharField(
        "CIN",
        primary_key=True,
        max_length=8,
        validators=[
            MaxLengthValidator(8,message="verifu length"),
            MinLengthValidator(8),
            only_int
        ]
        
    )
    username = models.CharField("Username", max_length=255, unique=True)
    email = models.EmailField(
        unique=True,
        validators=[RegexValidator(regex='[a-zA-Z0-9]+@esprit.tn', message="Esprit emails only")]
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "users"
