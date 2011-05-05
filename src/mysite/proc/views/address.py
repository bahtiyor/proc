# -*- coding: utf-8 -*-
'''
Created on 16.03.2011

@author: Admin
'''
from django.template import loader,Context,RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import request
from django.shortcuts import *
from mysite.proc.service_model import *
from mysite.proc.addres_model import *
from mysite.proc.views.forms import *

def address(request,s):
    s_list = Addres.objects.all()    
    return render( request,'address.html', {'s_list': s_list})

def address_form(request,id_):
    if request.method=='POST':
        a = Addres.objects.get(pk=id_)

        form=AddressForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/proc/address/')
        else:
            return render( request,'address_form.html', {'form': form})
    else:        
        s = Addres.objects.get(id=id_)
        form=AddressForm(instance=s)
        del_url="%s/delete" % id_
        
        return render( request,'address_form.html', {'form': form,'del_url': del_url})

def address_delete(request,id_):
        s = Addres.objects.get(id=id_)
        s.delete()
        return HttpResponseRedirect('/proc/address')

def address_form_add(request,id_=0):
    if request.method=='POST':
        form=AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/proc/address/')
        else:
            return render( request,'address_form.html', {'form': form})
    else:
        '''Добавление нового объекта'''
        form=AddressForm()      
        return render( request,'address_form.html', {'form': form})
