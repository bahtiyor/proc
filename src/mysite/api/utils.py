# -*- coding: utf-8 -*-

from piston.handler import BaseHandler
from mysite.proc.models import *
from mysite.proc.sys_class import *
from django.utils import simplejson

def isNoneId(obj):
    ''' Возвращает ID объекта если он не пустой(None)
        иначе возвращает None
    '''
    if obj is not None:
        return obj.id
    else:
        return None

def transfer( body_, login_, retval_):
    ''' Функция вставки нового платежа 
        ACT = 0
    '''    
    retval_["status"] = "0"
        
    tr = Transaction()                          # Инициируем новый объект Transaction
    
    
    try:
        ag = Agent.objects.filter(user__username = login_)[0]           # Достанем Агента
    
        # проверить есть ли перевод с таким же hesh_id от этого терминала
        try:
            trans = Transaction.objects.filter(agent=ag.id, hesh_id=body_["hesh_id"])
        except(Transaction.DoesNotExist):
            pass
        except Exception as inst:
            print type(inst)     # the exception instance
            print inst.args      # arguments stored in .args
            print inst
            retval_["status"] = "-1"
            return
            
        tr.opservices = OpService.objects.get(id= body_["id_uslugi"])
        tr.number_key = body_["nomer"]
        tr.summa = body_["summa"]
        tr.summa_pay = body_["summa_zachis"]
        tr.hesh_id = body_["hesh_id"]
        
        #TODO: Пока оставим это так
        tr.summa_commiss = tr.summa - tr.summa_pay 
        
        tr.agent = ag 
        
        tr.add(api = True)
    except(IndexError, Agent.DoesNotExist, OpService.DoesNotExist) :
        retval_["status"] = "-1"
    
    #return retval                                  # Если все нормально прошло то возвращается 0


def reg_sost( body_, login_, retval_):
    ''' Регистрация состояния терминала
        ACT = 1
    '''
    
    retval_["status"] = "0"
    
    try:
        ag = Agent.objects.filter(user__username = login_)[0]           # Достанем Агента
    except(IndexError, Agent.DoesNotExist) :
        try:
            ag = Agent.objects.filter(key_hash = login_)[0]           # Достанем Агента по хешу ключа
        except(IndexError, Agent.DoesNotExist) :
            retval_["status"] = "-1"
            return 0
    
    js = JourSostAgent()
    actS = ActualState()
    
    js.agent = ag
    actS.agent = ag
    
    
    if "date" in body_:
        js.date = body_["date"] #datetime.strptime(body_["date"],'YYYY-MM-DD HH:MI:ss')
        actS.date = js.date
    
    if "cash_count" in body_:
        js.cash_count = body_["cash_count"]
        actS.cash_count = js.cash_count
        
    if "link" in body_:
        js.link = bool(int(body_["link"]))
        actS.link = js.link
        
    if "cash_code" in body_:
        sa = SostAgent.objects.filter(type = "C", code = body_["cash_code"])[0]
        js.cash_code = sa
        actS.cash_code = js.cash_code
        
    if "printer" in body_:
        sa = SostAgent.objects.filter(type = "P", code = body_["printer"])[0]      
        js.printer = sa
        actS.printer = js.printer
        
    if "terminal" in body_:
        sa = SostAgent.objects.filter(type = "T", code = body_["terminal"])[0]
        js.terminal = sa
        actS.terminal = js.terminal
    
    # сохраним новый статус агента в журнале состояний
    js.save()
    
    # Очистим статус этого агента в таблице для мониторинга
    ActualState.objects.filter(agent=ag).delete()
    
    # И сохраним новый статус агента
    actS.save()

def get_time(retval_):
    ''' Возвращает текущую дату '''
    retval_["status"] = "0"
    retval_["body"] = str(datetime.now())

def get_opservices(login_, retval_):
    ''' Функция возвращает все доступные операторы услуг для заданного агента '''
    
    retval_["status"] = "0"
    
    try:
        id = Agent.objects.filter(user__username = login_)[0].id        # Достанем id Агента
    except(IndexError, Agent.DoesNotExist) :
        retval_["status"]="-1"
        return "-1"
    
    query="select o.* from proc_opservice o, proc_agent_opservices ao where o.id=ao.opservice_id and ao.agent_id= %s  union   select o.* from proc_opservice o, proc_agent_opservice_group aog, proc_opservicegroup_opservice ogo where  aog.opservicegroup_id=ogo.opservicegroup_id and aog.agent_id = %s" % (id, id)
    
    op = OpService.objects.raw(query)[0:]
    data = simplejson.dumps([{"id": o.id,"code": o.code, "name": o.name, "need_check": o.need_check, "mask": o.mask, "state": o.state.id, "type": o.type.id, "order": o.order} for o in op])
    retval_["body"] = data
    return 0
     

def get_optype(login_, retval_):
    ''' Функция возвращает все типы услуг'''
    
    retval_["status"] = "0"
    
    try:
        id = Agent.objects.filter(user__username = login_)[0].id        # Достанем id Агента
    except(IndexError, Agent.DoesNotExist) :
        retval_["status"]="-1"
        return "-1"
           
    opt = ServiceType.objects.all()
    data = simplejson.dumps([{"id": o.id,"code": o.code, "name": o.name, "parent": isNoneId(o.parent), "order": o.order} for o in opt])
    retval_["body"] = data
    return 0




def do_job(act_, body_, login_, retval_):
    ''' Функция обработки команд '''        
    
    retval_["status"] = "0"
    
    if act_ == "0":                                 # Новый платеж
        transfer( body_, login_, retval_)
    elif act_ == "1":                               # Для журналирования состояния
        reg_sost( body_, login_, retval_)
        ret = "0"        
    elif act_ == "2":                               # Запрос текущего времени
        ret = get_time(retval_);
    elif act_ == "5":                               # Запрос типов операторов услуг
        ret = get_optype(login_, retval_);
    elif act_ == "6":                               # Запрос доступных операторов услуг
        ret = get_opservices(login_, retval_);
        
    
    