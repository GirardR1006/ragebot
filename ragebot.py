import os
import time
from slackclient import SlackClient

#BOT ID FROM ENV VARIABLE, WON'T WRITE IT THERE. 
BOT_TOKEN=os.environ.get('SLACKBOT_TOKEN')

#SLACK API INSTANCIATION, TO CHECK WHERE WILL THE HATE BE POURED ON
slack_client = SlackClient(BOT_TOKEN)

def express_pure_rage(CHANNEL, MESSAGE):
    """
        RECEIVES MESSAGE FROM CHANNEL, CHECK IF IT'S UPPERCASE. IF NOT, 
        WILL YELL AT USER.
    """        
    if not MESSAGE.isupper():
        RESPONSE = "ICI, ON ÉCRIT EN MAJUSCULE! TU DEVRAIS ÉCRIRE: " + MESSAGE.upper() 
        slack_client.api_call("chat.postMessage", channel=CHANNEL, text=RESPONSE, as_user=True)


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output:
                #RETURN ALL NEEDED INFORMATION TO DECIDE WHETHER OR NOT THE USER
                #SHOULD DIE
                return output['text'], output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 SECOND DELAY BETWEEN READINGS 
    if slack_client.rtm_connect():
        print("RAGEBOT IS CONNECTED! REEEEEEEEEE")
        while True:
            MESSAGE, CHANNEL = parse_slack_output(slack_client.rtm_read())
            #THE HECK WITH STRING BEING BOOLEAN"""
            if MESSAGE and CHANNEL:
                express_pure_rage(CHANNEL, MESSAGE)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("CONNECTION FAILED! CHECK YOUR BOT TOKEN YOU DAMNED NORMIE!")

