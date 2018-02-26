from django.db import models
from django.utils import timezone

class Sms(models.Model):
    #name of the sender to be displayed to the receiver
    sender_name = models.CharField(max_length=200)
    #receiver field stores the receivers number. What if number starts with zero 0???
    receiver = models.CharField(max_length=12) 
    #title of the sms
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_sent = models.DateTimeField(
            default=timezone.now)

    #def send(sms):
        #defined the send sms method in utils file
        #using builtin method from djexmo to send sms
        #response = send_message(to='+recr', text=text_to_send)
        #self.save()
	
	#__str__(self) will be used to check what message has been sent
    def __str__(self):
        return "Title: " + self.title + ", Text: " + self.text
