#send texts without sharing #s. send security code to login/pw
#send daily deals
#twilio is external package, not within python - dl via instructor notes


from twilio import rest

#Your account id and pw from twilio.com/user/account
account_sid = "AC32a3c49700934481addd5ce1659f04d2"
auth_token = ""
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "Boom boom pow, these chickens jockin yo style",
    to= "+16502222222"      #my number
    from = "+16502222222")  #twilio number

print message.sid

#notes
# import fxns or attributes from packages or modules
# twilio > rest > py file with class TwilioRestClient
# from twilio.rest import TwilioRestClient
# twilio mod has rest mod has class TwilioRestClient has def __init fxn

# brad = turtle.Turtle()
# in py is a file called turtle, and in there is a class turtle.
# class Turtle():
#   def __init__():
# brad object can then use all the other fxns like forward

#client = rest.TwilioRestClient()
#in Twilio is folder rest. in folder rest is py file with a class TwilioRestClt
# class TwilioRestClient():
#   def __init__():
# object client can then do fxns defined in that class - like send sms

#class like turtle (info on how to make it forward, turn)
# can create instances like brad or angie

#class TRC (info on how to connect, send sms)
# can create instance - 1 client - send text etc

# what is a class?
# what is an instance of a class?
# another analogy of the 2 other than a blueprint?
#check online

#create an instance brad of class turtle, then brad.forward(100)
#create an instance quotes of type file, then quotes.read()
#create a file-like instance 'connection' of class urllib, then connection.read()
