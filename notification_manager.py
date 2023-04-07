from twilio.rest import Client

TWILIO_SID = "ACe5b3b6f0719f55a8ff4a33d03cbf07fe"
TWILIO_AUTH_TOKEN = "746820c864373474ecc5cda529d98a30"
TWILIO_VIRTUAL_NUMBER = "+19125134384"
TWILIO_VERIFIED_NUMBER = "+4915738321885"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.Client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message =self.Client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)