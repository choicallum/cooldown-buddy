import requests
import pprint

pre_key = "?api_key="
api_key = #CHECK REPO FOR STEPS TO GET YOUR OWN API_KEY

api_base_url = "https://na1.api.riotgames.com"
summonerName = input("Enter the summoner name of the in-game player: ")
summoner_endpoint_path = f"/lol/summoner/v4/summoners/by-name/{summonerName}"

summoner_endpoint = f"{api_base_url}{summoner_endpoint_path}{pre_key}{api_key}"
r1 = requests.get(summoner_endpoint)

def error_msg(status_code):
    print("Sorry, an error has occurred. Error Code: " + str(status_code))
    exit()

if r1.status_code in range(200, 299):
    summonerData = r1.json()
    summonerID = summonerData['id']
else: 
    error_msg(r1.status_code)

live_game_endpoint_path = f"/lol/spectator/v4/active-games/by-summoner/{summonerID}"
livegame_endpoint = f"{api_base_url}{live_game_endpoint_path}{pre_key}{api_key}"
r2 = requests.get(livegame_endpoint)

if r2.status_code in range(200,299):
    liveGame = r2.json()
else:
    error_msg(r2.status_code)

champKeys = []

for i in range(10):
    champKeys.append(liveGame['participants'][i]['championId'])

print(champKeys)
champData = requests.get('http://ddragon.leagueoflegends.com/cdn/11.18.1/data/en_US/championFull.json').json()

champNames= []
for j in range(10):
    champNames.append(champData['keys'][str(champKeys[j])])

spellOrder = ["Q", "W", "E", "R"]

for k in range(10):
    print(champNames[k] + ":\n")
    for p in range(4):
        print(spellOrder[p] + ": " + champData['data'][champNames[k]]['spells'][p]['cooldownBurn'])
    print("\n")
