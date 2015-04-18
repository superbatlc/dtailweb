from django.db import models
from calls.models import Call
from systems.models import System

class Phonegroup(models.Model):
    """
    PhoneGroup
    
    Defines phonegroup details and father to son relationship
    if exists or parent_id = id otherwise.
    """
    parent = models.ForeignKey('self',blank=True, null=True, help_text="The father of this group",related_name="child_phonegroup_set")
    name = models.CharField(max_length=255, verbose_name="Nome")
    code = models.CharField(max_length=10, verbose_name="Codice")


class PhonegroupExtension(models.Model):
    """
    PhonegroupExtension
    
    Defines the relationship between an extension of a system and the
    phonegroup it belongs to.
    """
    phonegroup = models.ForeignKey(Phonegroup)
    extension = models.CharField(max_length=4)
    system  = models.ForeignKey(System)



class PhonegroupCall(models.Model):
    """
    PhonegroupCall
    
    Relation between the call and the phonegroups in which the extension who
    originated the call belongs to at the moment.
    """
    call = models.ForeignKey(Call)
    phonegroup = models.ForeignKey(Phonegroup)
    