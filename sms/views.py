from django.shortcuts import render
from .models import Sms
from .forms import SendSmsForm
from django.shortcuts import redirect
from django.utils import timezone
from .utils import send_sms_using_nexmo

def sent_messages(request):
    messages = Sms.objects.all().order_by('date_sent')
    return render(request, 'sms/sent_messages.html', {'messages': messages})

def message_detail(request):
    return render(request, 'sms/message_detail.html', {'response': response})

def send_sms_view(request):
    if request.method == "POST":
        form = SendSmsForm(request.POST)
        if form.is_valid():
            sms = form.save(commit=False)
            sms.date_sent = timezone.now()
            #sms.save()

            response = send_sms_using_nexmo(sms)
            response = response['messages'][0]
            
            #response = {'status': '0', 'to': 7, 'from': 'First', 'keyword': 7, 'text': 'First', 'timestamp': '0', 'balance': 7, 'count': 'First', 'price': 7, 'error-text':'Get lost'}
            #print (response['status'])
            if (response['status'] == '0'):
                print ("now here----------------")
                return render(request, 'sms/message_detail.html', {'response': response})
            else:
                print('Error:', response['error-text'])

    else:
        form = SendSmsForm()
    return render(request, 'sms/send_sms_view.html', {'form': form})
