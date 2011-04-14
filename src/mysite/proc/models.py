import datetime

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User 
from mysite.proc.service_model import *
from mysite.proc.addres_model import *
from mysite.proc.sys_model import *
from mysite.proc.tarif_model import *


AGENT_TYPE = (
        ('T', 'Terminal'),
        ('M', 'Mobile'),
        ('W', 'Web'),
    )


class Dealer(models.Model):
    account         =models.CharField(max_length=8,blank=True)
    addresses       = generic.GenericRelation( Addres, null=True, blank=True )        
    check_for_ip    =models.BooleanField(default=False)
    #date_create     =models.DateTimeField(auto_now_add=True)
    #date_last_visit =models.DateTimeField( null=True, blank=True)
    dealer          =models.ForeignKey('self',related_name='parent', null=True, blank=True)
    #email           =models.EmailField(blank=True)    
    inn             =models.CharField(max_length=12,blank=True)
    ipaddresses     = generic.GenericRelation( IpAddress, null=True, blank=True )
    kopf            =models.ForeignKey(Kopf)
    limit           =models.FloatField(blank=True)
    #login           =models.CharField(max_length=20,unique=True)
    #name            =models.CharField(max_length=50)
    overdraft       =models.FloatField(blank=True)
    #password        =models.CharField(max_length=100)
    tel             =models.CharField(max_length=20,blank=True)    
    state           =models.ForeignKey(State)
    summa           =models.FloatField(blank=True)
    user            =models.OneToOneField(User, blank=True)
    
    def __unicode__(self):
        return self.user.username
    
    def __str__(self):
        return self.user.username

class Agent(models.Model):
    addresses = generic.GenericRelation( Addres, null=True, blank=True )    
    check_for_ip    =models.BooleanField(default=False)
    #date_create     =models.DateTimeField(auto_now_add=True)
    #date_last_visit =models.DateTimeField(auto_now_add=True)
    dealer          =models.ForeignKey(Dealer, null=True, blank= True)
    #email           =models.EmailField(blank=True)
    name            =models.CharField(max_length=50)
    imei            =models.CharField(max_length=20,blank=True)
    ipaddresses     = generic.GenericRelation( IpAddress, null=True, blank=True )
    #login           =models.CharField(max_length=20,unique=True)
    opservices      =models.ManyToManyField(OpService, null=True, blank=True)
    opservice_group =models.ManyToManyField(OpServiceGroup)
    #password        =models.CharField(max_length=100)
    tarif_profile_arr=models.ManyToManyField(TarifProfile)
    tel             =models.CharField(max_length=20,blank=True)
    type            =models.CharField(max_length=1,choices=AGENT_TYPE)
    state           =models.ForeignKey(State)
    user            =models.OneToOneField(User, blank=True)
    
    def __unicode__(self):
        return self.name
    
class Transaction(models.Model):
    agent           =models.ForeignKey(Agent)    
    date            =models.DateTimeField(auto_now_add=True)
    opservices      =models.ForeignKey(OpService)
    number_key      =models.CharField(max_length=100)
    summa           =models.FloatField()
    summa_commiss   =models.FloatField()
    summa_pay       =models.FloatField()    
    state           =models.ForeignKey(State)
    coment          =models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.summa
    
class ArcMove(models.Model):
    date            =models.DateTimeField(auto_now_add=True)
    dealer          =models.ForeignKey(Dealer)
    dt              =models.BooleanField()    
    saldo           =models.FloatField()
    summa           =models.FloatField()
    transaction     =models.ForeignKey(Transaction)

    
    
    def __unicode__(self):
        return self.summa