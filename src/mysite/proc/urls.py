from django.conf.urls.defaults import *
from django.conf.project_template.urls import urlpatterns
from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from mysite.proc.views import *
from mysite.proc.views import service
from mysite.proc.views import address
from mysite.proc.views import tarif
from mysite.proc.views import dealer
from mysite.proc.views import account
from mysite.proc.views import system
from mysite.proc.views import transaction
from mysite.proc.views import monitor
from mysite.proc.views import grids



urlpatterns=patterns('',
    #url(r'^$', system.main),
    (r'^grid/', include('mysite.proc.urls_grid')),    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    (r'^accounts/login/$',  account.login),
    (r'^accounts/logout/$', account.logout),

    (r'^$', system.to_main),
    (r'^main/$', system.main),    
    
    (r'^pay/$', transaction.pay_list),
    (r'^pay/(\d+)$', transaction.pay_form),
    (r'^pay/(\d+)/delete$', transaction.pay_delete),
    (r'^pay/add$', transaction.pay_form_add),
    (r'^pay/add/(\d+)$', transaction.pay_form),
    (r'^pay/add/(\d+)/delete$', transaction.pay_delete),        

    (r'^fill_ac/add$', transaction.fill_ac_form_add),
    
    (r'^service_type/$', service.service_type),
    (r'^service_type/(\d+)$', service.service_type_form),
    (r'^service_type/(\d+)/delete$', service.service_type_delete),
    (r'^service_type/add$', service.service_type_form_add),
    (r'^service_type/add/(\d+)$', service.service_type_form),
    (r'^service_type/add/(\d+)/delete$', service.service_type_delete),
    
    # =============== OP_SERVICE =================
    (r'^op_service/$', service.op_service),
    (r'^op_service/(\d+)$', service.op_service_form),
    (r'^op_service/(\d+)/delete$', service.op_service_delete),
    (r'^op_service/add$', service.op_service_form_add),
    (r'^op_service/add/(\d+)$', service.op_service_form),
    (r'^op_service/add/(\d+)/delete$', service.op_service_delete),
    
    # ============== OP_SERVICE_GROUP ============
    (r'^op_service_group/$', service.op_service_group),
    (r'^op_service_group/(\d+)$', service.op_service_group_form),
    (r'^op_service_group/(\d+)/delete$', service.op_service_group_delete),
    (r'^op_service_group/add$', service.op_service_group_form_add),
    (r'^op_service_group/add/(\d+)$', service.op_service_group_form),
    (r'^op_service_group/add/(\d+)/delete$', service.op_service_group_delete),
    
    # ============== ADDRESS ============
    (r'^address/(?P<id_>\d+)/(?P<content>\w+)$', address.address),                              # view
    (r'^address/add/(?P<id_>\d+)/(?P<content>\w+)$', address.address_form_add),                 # add
    (r'^address/(?P<id_>\d+)/(?P<content>\w+)/(?P<aid_>\d+)$', address.address_form),           # edit
    (r'^address/(?P<id_>\d+)/(?P<content>\w+)/(?P<aid_>\d+)/delete$', address.address_delete),  # delete
    # ============== IP ADDRESS ============
    (r'^ipaddress/(?P<id_>\d+)/(?P<content>\w+)$', address.ipaddress),                              # view
    (r'^ipaddress/add/(?P<id_>\d+)/(?P<content>\w+)$', address.ipaddress_form_add),                 # add
    (r'^ipaddress/(?P<id_>\d+)/(?P<content>\w+)/(?P<aid_>\d+)$', address.ipaddress_form),           # edit
    (r'^ipaddress/(?P<id_>\d+)/(?P<content>\w+)/(?P<aid_>\d+)/delete$', address.ipaddress_delete),  # delete
    
    # ============== TARIF_ARR ============
    (r'^tarif_arr/(\d+)$', tarif.tarif_arr),
    (r'^tarif_arr/(\d+)/(\d+)$', tarif.tarif_arr_form),
    (r'^tarif_arr/(\d+)/(\d+)/delete$', tarif.tarif_arr_delete),
    (r'^tarif_arr/(\d+)/add$', tarif.tarif_arr_form_add),
    (r'^tarif_arr/(\d+)/add/(\d+)$', tarif.tarif_arr_form),
    (r'^tarif_arr/(\d+)/add/(\d+)/delete$', tarif.tarif_arr_delete),
    # ============== TARIF ================
    (r'^tarif/$', tarif.tarif),
    (r'^tarif/(\d+)$', tarif.tarif_form),
    (r'^tarif/(\d+)/delete$', tarif.tarif_delete),
    (r'^tarif/add$', tarif.tarif_form_add),
    (r'^tarif/add/(\d+)$', tarif.tarif_form),
    (r'^tarif/add/(\d+)/delete$', tarif.tarif_delete),
    # ============== TARIF GROUP ================
    (r'^tarif_group/$', tarif.tarif_group),
    (r'^tarif_group/(\d+)$', tarif.tarif_group_form),
    (r'^tarif_group/(\d+)/delete$', tarif.tarif_group_delete),
    (r'^tarif_group/add$', tarif.tarif_group_form_add),
    (r'^tarif_group/add/(\d+)$', tarif.tarif_group_form),
    (r'^tarif_group/add/(\d+)/delete$', tarif.tarif_group_delete),
    # ============== TARIF PROFILE ===============
    (r'^tarif_profile/$', tarif.tarif_profile),
    (r'^tarif_profile/(\d+)$', tarif.tarif_profile_form),
    (r'^tarif_profile/(\d+)/delete$', tarif.tarif_profile_delete),
    (r'^tarif_profile/add$', tarif.tarif_profile_form_add),
    (r'^tarif_profile/add/(\d+)$', tarif.tarif_profile_form),
    (r'^tarif_profile/add/(\d+)/delete$', tarif.tarif_profile_delete),
    # ============== DEALER ===============
    (r'^dealer/$', dealer.dealer),
    (r'^dealer/(\d+)$', dealer.dealer_form),
    (r'^dealer/(\d+)/delete$', dealer.dealer_delete),
    (r'^dealer/add$', dealer.dealer_form_add),
    (r'^dealer/add/(\d+)$', dealer.dealer_form),
    (r'^dealer/add/(\d+)/delete$', dealer.dealer_delete),
    # ============== AGENT ===============
    (r'^agent/$', dealer.agent),
    (r'^agent/(\d+)$', dealer.agent_form),
    (r'^agent/(\d+)/delete$', dealer.agent_delete),
    (r'^agent/add$', dealer.agent_form_add),
    (r'^agent/add/(\d+)$', dealer.agent_form),
    (r'^agent/add/(\d+)/delete$', dealer.agent_delete),
    # ============== MONITORING ===============
    (r'^monitor/$', monitor.show),
    (r'^monitor/logs/(\d+)$', monitor.journal),
    
    url (r'^gridmonitor/$', grids.grid_handler, name='grid_handler'), 
    url (r'^gridmonitor/cfg/$', grids.grid_config, name='grid_config'),
    
    #(r'^login/$', login_view),
    #(r'^contact/$', contact),
    #(r'^contact_form/$', contact_form),
    
    
                     
)