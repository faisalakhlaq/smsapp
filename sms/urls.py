from django.conf.urls import url
from . import views
#from django.conf.urls import patterns, url

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'send_sms_view/', views.send_sms_view, name='send_sms_view'),
    url(r'sent_messages/', views.sent_messages, name='sent_messages'),
    url(r'^$', views.sent_messages, name='sent_messages'),
    url(r'message_detail/', views.message_detail, name='message_detail'),

    url(r'^sms/new/$', views.send_sms_view, name='new_sms'),
#    url(r'^nexmo/', include('djexmo.urls')),
]

