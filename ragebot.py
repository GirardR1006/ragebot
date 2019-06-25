import os
import time
import slack

#BOT ID FROM ENV VARIABLE, WON'T WRITE IT THERE. 
bot_token = os.environ.get('SLACKBOT_TOKEN')

#SLACK API INSTANCIATION, TO CHECK WHERE WILL THE HATE BE POURED ON
slack_client = slack.WebClient(token=bot_token)

@slack.RTMClient.run_on(event='message')
def express_pure_rage(**payload):
    #RETURN ALL NEEDED INFORMATION TO DECIDE WHETHER OR NOT THE USER
    #SHOULD DIE
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    MESSAGE = data['text']
    if not MESSAGE.isupper():
        RESPONSE = "ICI, ON ÉCRIT EN MAJUSCULE! TU DEVRAIS ÉCRIRE: " + MESSAGE.upper() 
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']
        
        web_client.chat_postMessage(
        channel=channel_id,
        text=RESPONSE
        )
    
if __name__ == "__main__":
    if slack_client.rtm_connect():
        print("RAGEBOT IS CONNECTED! REEEEEEEEEE")
        rtm_client = slack.RTMClient(token=bot_token)
        rtm_client.start()
    else:
        print("CONNECTION FAILED! CHECK YOUR BOT TOKEN YOU DAMNED NORMIE!")

