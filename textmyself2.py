from twilio.rest import Client

def textmyself(message, number):
    accountSID = 'Your ID here'
    authToken = 'Your token here'
    myTwilioNumber = 'Your Twilio number here'
    myCellPhone = number
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)

def textimg(img, message, number):
    accountSID = 'Your ID here'
    authToken = 'Your token here'
    myTwilioNumber = 'Your Twilio number here'
    myCellPhone = number
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone, media_url=img)
