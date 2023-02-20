from django.contrib import admin,messages
from .models import *


class ParticipationInline(admin.StackedInline):# affiche fel add les participants par defaut  TabularInline ou StackedInline
    model=Participation
    extra=1 
    readonly_fields=('datePart',)
    can_delete=False
#@admin.register(Event) ya hethi yaa tamel register fel louta
def set_Accept(ModelAdmin,request,queryset):
    rows=queryset.update(state=True)
    if rows ==1:
        message="one event was"
    else:
        message=f"{rows} events were"
    messages.success(request,message="%succesufully accepted"%message)
set_Accept.short_description='Accept' #ajouter dans Action


class ParticipateListFilter(admin.SimpleListFilter):
    title="Participation"
    parameter_name='nbrParticipants'
    def lookups(self, request, model_admin): # affichage ll user 
        return (
            ('0','No Participants'),
            ('more','there are participants'),
        )
    def queryset(self, request, queryset):# communiquer avec base de donnees 
        if self.value()=='0':
            return queryset.filter(nbrParticipants__exact=0)
        if self.value()=='more':
            return queryset.filter(nbrParticipants__gt=0)# > 0
class EventAdmin(admin.ModelAdmin):
    def set_Refuse(self,request,queryset):
        rows=queryset.filter(state=False)
        if rows.count()>0:
            messages.error(request,message=f"{rows}events aready refused")
        else:
            rows=queryset.update(state=False)
            if rows ==1:
                message="one event was"
            else:
                message=f"{rows} events were"
            messages.success(request,message="%succesufully refused"%message)
    set_Refuse.short_description='Refuse'           
    actions=[set_Accept,"set_Refuse"]
    inlines=[
        ParticipationInline
    ]
    list_display=(
        'title',
        'category',
        'state'
    )  # yakhtar les attribues eli bech yafichehom 
    ordering=('title',)

    list_filter=('state','category',ParticipateListFilter)
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
                        'eventDate',
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
admin.site.register(Participation)
