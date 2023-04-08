from twilio.rest import Client
import smtplib

TWILIO_SID = "ACe5b3b6f0719f55a8ff4a33d03cbf07fe"
TWILIO_AUTH_TOKEN = "746820c864373474ecc5cda529d98a30"
TWILIO_VIRTUAL_NUMBER = "+19125134384"
TWILIO_VERIFIED_NUMBER = "+4915738321885"
my_email = "minhphi.nguyen91@gmail.com"
password ="gkytuckgjfesrtlh"

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

    def send_emails(self,  emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
