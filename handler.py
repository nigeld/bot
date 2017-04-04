def recived_mesagge(event):
    sender_id = event['sender']['id']
    recipient_id = event['recipient']['id']
    message = event['message']
    text = message['text']

    print(sender_id)
    print(recipient_id)
    print(text)
