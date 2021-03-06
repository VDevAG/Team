import random
import sys
import json


jsonText = open('statistics.json', 'r').read()
players = json.loads(jsonText)

legalTeamSize = 9

def getPlayersWithMostGames():    
    mostGames = max(players.values())
    playersWithMostGames = []
    for player in players:
        if(players[player] == mostGames):
            playersWithMostGames.append(player)
    return playersWithMostGames


def playersToKick(playersWithMostGames, dontWantToPlay):
    potentialKick = playersWithMostGames
    playersToKick = []
    while legalTeamSize != len(players) - len(playersToKick):
        choosenPlayer = random.choice(potentialKick)
        playersToKick.append(choosenPlayer)
    return playersToKick

def getTeam(kickedPlayers):
    team = []
    for player in players:
        if not player in kickedPlayers:
            team.append(player)
    return team

def getKicked(args, kickPlayers):
    return args[1:] + kickPlayers

def main():
    stringArgs = []
    for s in sys.argv:
        stringArgs.append(str(s))
    for i in stringArgs[1:]:
        del players[i]
    playersWithMostGames = getPlayersWithMostGames()
    kickPlayers= playersToKick(playersWithMostGames,stringArgs)
    team = getTeam(kickPlayers)
    resting = getKicked(stringArgs, kickPlayers)
    print(f"{team} spelar och {resting} vilar")


if __name__ == '__main__':
    main()