#!C:/Users/AKHIL M K/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")


from twilio.rest import Client
account_sid = 'AC114b9495458649a06a63c604c5ba3749'
auth_token = '09e3d8cf1b5cb227d761b84b04189c02'
client = Client(account_sid, auth_token)
message = client.messages.create(from_='+15674722313',
                          to='+916379482851',
                          body='hai shiva i am akil')
