from django.contrib import admin
from .models import *

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=(
        'username',
        'cin',
        'email'
    )  # yakhtar les attribues eli bech yafichehom 
    #ordering=('userAdmin',)

    list_filter=('cin','username')
admin.site.register(Person,userAdmin)
