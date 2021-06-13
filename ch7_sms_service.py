from twilio.rest import Client

account_sid = 'your account_sid'
auth_token = 'your auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
	to="your phone number",
	from_= 'twilio number',
	body="sms text")