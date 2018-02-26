import nexmo

from django.conf import settings

#def send_sms_using_nexmo(frm=None, to=None, text=None):
def send_sms_using_nexmo(form):
    """Shortcut to send a sms using libnexmo api.
    :param frm: The originator of the message
    :param to: The message's recipient
    :param text: The text message body
    Example usage:
    >>> send_message(to='+33123456789', text='My sms message body')
    """

    txt = form.text
    titl = form.title
    to = form.receiver
    text_to_send = titl +"\n "+ txt 

    assert to is not None
    assert txt is not None

#    if frm is None:
    frm = settings.NEXMO_DEFAULT_FROM

    client = nexmo.Client(key=settings.NEXMO_API_KEY, secret=settings.NEXMO_API_SECRET)
    response = client.send_message({
        'from': frm,
        'to': to,
        'text': text_to_send
    })
    return response
