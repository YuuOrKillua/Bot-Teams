import asyncio
from asyncore import loop
import pymsteams;
import json;

def botTeams():
    #váriavel de arroba por que sera usada muitas vezes
    arroba = '@'
    #váriavel de arroba por que sera usada muitas vezes
    #variaveis do json
    #leitor de json
    with open("Aprecie.json", encoding='utf-8') as aprecie_json:
        aprecie = json.load(aprecie_json)
    print(aprecie)
    #leitor de json
    for i in aprecie:
        reconhecido = (i['nome1'])
        apreciador = (i['nome2'])
        email_reconhecido = (i['email1'])
        email_apreciador = (i['email2'])
    #variaveis do json
    #pymsteams é api desse código
    myTeamsMessage = pymsteams.connectorcard("<Microsoft Webhook URL>")
    myTeamsMessage.payload = {
        "type": "message",
        "attachments": [
            {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "type": "AdaptiveCard",
                "body": [
                    {
                        "type": "TextBlock",
                        "text": "Hello " + arroba + email_reconhecido + "voce foi rechonecido por " + arroba + email_apreciador
                    }
                ],
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.0",
                "msteams": {
                    "entities": [
                        {
                            "type": "mention",
                            "text": "<at>Leonardo</at>",
                            "mentioned": {
                                "id": arroba + email_reconhecido,
                                "name": reconhecido + apreciador
                            }
                        }
                    ]
                }
            }
        }]
    }
    myTeamsMessage.send()
if __name__ == '__main__':
    botTeams()