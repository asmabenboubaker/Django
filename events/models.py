import datetime
from django.db import models
from users.models import *
from django.core.exceptions import ValidationError
# Create your models here.

def titleValidator(value):
    if not value.istitle():
        raise ValidationError(
            "Title must contain capital letters"
        )
def ValidatorDate(date):
    if date<datetime.date.today():
        raise ValidationError(
            " date must be greater than today"
        )
class Event(models.Model):
    CATEGORY_CHOICES = (
        ('Music', 'Music'),
        ('Cinema', 'Cinema'),
        ('Sport', 'Sport'),
    )

    title = models.CharField(max_length=255, null=True,validators=[
        titleValidator
    ])
    description = models.TextField()
    eventImage = models.ImageField(upload_to='images/', blank=True)

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=8)
    state = models.BooleanField(default=False)
    nbrParticipants = models.IntegerField(default=0)
    eventDate = models.DateField(validators=[ValidatorDate])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organizer= models.ForeignKey(Person,
    on_delete=models.CASCADE)


    def __str__(self):
        return self.title

