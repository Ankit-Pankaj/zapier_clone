from integrations.slack import SlackIntegration
from integrations.gmail import GmailIntegration

slack = SlackIntegration({'username':'ankit', 'password':'plain_password'})

channels = slack.get_channels({'title':'abc'})


def get_channels():
    try:
        slack = SlackIntegration({'username':'ankit', 'password':'plain_password'})
        channels = slack.get_channels({'title':'abc'})
        print(channels)
    except Exception as e:
        raise Exception(e)
    
def send_email():
    try:
        gmail = GmailIntegration({'username':'ankit', 'password':'plain_password'})
        data = gmail.send_email({'subject':'Test Email', 'recipient':'ankit@gmail.com', 'content':'email content'})
        print(data)
    except Exception as e:
        raise Exception(e)
    
def check_failure():
    try:
    
        slack = SlackIntegration('plain_password')
        channels = slack.get_channels({'title':'abc'})
    except Exception as e:
        raise Exception(e)
   
get_channels()
send_email()
# check_failure()