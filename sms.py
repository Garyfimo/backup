from twilio.rest import TwilioRestClient
 
account_sid = "ACbd337257c8ddde9adc5e720bb0405119"
auth_token = "ff76e3e5409738adbb027ebb6e6f0aca"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(
        body ="ola que ase :)", # mensaje
        to = "+51959821390", # remplazamos con nuestro numero o al que queramos enviar el sms
        from_= "+5117071368") # el numero que nos asigno twilio
 
print message.sid