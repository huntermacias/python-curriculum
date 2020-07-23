from twilio.rest import Client 
 
account_sid = 'ACf7a74abd150e43b86052874aa9079307' 
auth_token = 'f8792b128c5464d83acaa8727de7cf3b' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+17602784344',  
                              body='hey there hunter',      
                              to='+15594588379' 
                          ) 
 
print(message.sid)