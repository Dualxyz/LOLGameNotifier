# LOLGameNotifier

## Description:
A tool that allows you to track when a particular user enters a game in league of legends and sends you a notification through Discord's webhook to your server. Made in python3.

## Python library requirements:
```
pip install -r requirements.txt
```

## Setup:
Import the required information on line 32, 33, 34, 35 (line 36 is optional). 
- Getting Discord's webhook url: Create a server on Discord > Server settings > Integrations > Webhooks > New Webhook > Copy webhook URL (And optional set a special channel where you want the bot to type to)
- Valid values for Region:

![](https://i.imgur.com/KQtN7FB.png)
- summoner_name: Import the ign of the person which you want to track.
- api_key: Register on https://developer.riotgames.com/ to obtain the API key.
## Example:
```
webhook_url = "https://discord.com/api/webhooks/883390660768583740/lvwF9kX0jIs50wypxJzPCNo-GkhVpFii56xdwCfZmy1u4JoyD81JNhaQ1lKRN0-WzZzy"
region = "euw1"
summoner_name = "Duαl"
api_key = "RGAPI-39023e20-f474-4f13-898c-338956e77e94"
```

## Example of the output:

![](https://i.imgur.com/pM767ad.png)

## Features:
- Automatically checks every 5 minutes whether the person has entered.
- Displays the igns of all players in the current match.

## To-do list:
- Add multi user search.
- Make the result output on discord prettier.
- Add the division of all the players in the game.
- Add a recently played with section.
- Clean the code a little bit - but this is enough for the initial version. 
