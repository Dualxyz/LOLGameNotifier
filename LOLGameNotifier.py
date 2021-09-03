import requests;
from discord import Webhook, RequestsWebhookAdapter
import time;

class Summoner:
    def __init__(self, encryptedID = 0, accountID = 0, puUID = 0, name = 0):
        self.encryptedID = encryptedID;
        self.accountID = accountID;
        self.puUID = puUID;
        self.name = name;

    def printinfo(self):
        print("EncryptedID: " + str(self.encryptedID));
        print("accountID: " + str(self.accountID));
        print("puUID: " + str(self.puUID));
        print("name: " + str(self.name));

def requestData(region, summoner_name, api_key):
    url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key;
    response = requests.get(url);
    return response.json();

def checkGameStatus(region, encryptedID, api_key):
    url = "https://" + region + ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + encryptedID + "?api_key=" + api_key;
    response = requests.get(url);
    return response.json();

if __name__ == "__main__":
    gameId_old = "1";
    while(True):
        #IMPORT STUFF HERE
        webhook_url = "";       #import your discord webhook here
        region = "";            #import the region of the account you want to track (for euw type euw1; for eune type eun1; for na type na1)
        summoner_name = "";     #import the ign of the summoner you want to track
        api_key = "";           #import your riotdev API key (Make an account here https://developer.riotgames.com/ and paste the API key that's given to you)
        time_interval = 300;    #Time interval on when the check will be performed (by default it's 5 minutes - 300 seconds)
        ##################################################################################################################

        webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter());

        resJSON_requestData = requestData(region, summoner_name, api_key);
        encryptedID = str(resJSON_requestData['id']);
        accountID = str(resJSON_requestData['accountId']);
        puUID = str(resJSON_requestData['puuid']);
        name = str(resJSON_requestData['name']);

        sum1 = Summoner(encryptedID, accountID, puUID, name);
        #sum1.printinfo();
        resJSON_checkGameStatus = checkGameStatus(region, encryptedID, api_key);
        try:
            matchStatus = str(resJSON_checkGameStatus["status"]["status_code"]);
            time.sleep(time_interval);
            #print("User is not in game");
            #response = webhook.send("> User: " + summoner_name + " is not in game");
        except:
            gameId = resJSON_checkGameStatus['gameId'];
            if (gameId_old != gameId):
                gameMode = resJSON_checkGameStatus['gameMode'];
                gameType = resJSON_checkGameStatus['gameType'];
                #participants = (resJSON_checkGameStatus['participants']);
                participants = [];
                
                for entry in resJSON_checkGameStatus["participants"]:
                    #print(entry['summonerName']);
                    participants.append(entry['summonerName'])
                
                #print("User: " + summoner_name + "is in game.");
                response = webhook.send(f'''
                > User: **{summoner_name}** is in game.
                > gameMode: **{gameMode}**.
                > gameType: **{gameType}**.
                > 
                > **B L U E  S I D E**:
                > {participants[0]}
                > {participants[1]}
                > {participants[2]}
                > {participants[3]}
                > {participants[4]}
                > 
                > **R E D  S I D E**: 
                > {participants[5]}
                > {participants[6]}
                > {participants[7]}
                > {participants[8]}
                > {participants[9]}
                ''');
                gameId_old = gameId;
            else:
                time.sleep(time_interval);
