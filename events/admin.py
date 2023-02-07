from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'category',
        'state'
    )  # yakhtar les attribues eli bech yafichehom 
    ordering=('title',)

    list_filter=('state','category')
# recherche 
    search_fields=[
        'title',
        'category'
    ]
#pagination 
    list_per_page=5
# changer l'ordre du formulaire
    # fields=(

    #     'organizer',
    #     'state',
    #     ('title','description'),
    #     'eventImage',
    #     'nbrParticipants',
    #     'eventDate',
    #      'created_at',
    #     'updated_at'

    # )
    fieldsets = (
        (
            "State",
            {
                'classes':('collapse',),
                'fields':(('state','category'),
                ('created_at', 'updated_at'))
            }
            ),
            (
                'ABOUT',
                {
                    'fields':(
                        'title',
                        'description',
                        'nbrParticipants',
                        'eventImage',
                        'eventDate'
                    )
                }
            )
        )
    
    
    readonly_fields=(
        'created_at',
        'updated_at'
    )

# Register your models here.
admin.site.register(Event,EventAdmin)
