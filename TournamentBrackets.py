import random
import math


'''
Assuming we want random seed order meaning we can randomize
list right off the back. 

Single elimination no losers bracket

Levels or rounds are determined by log(n)

'''

#pretty stuff
def TopBox():
    print '\n|-------------------------|'
    #print '|                       |'

def BottomBox():
    #print '|                       |'
    print '|-------------------------|\n'
  


def PrintPlayers(players):
    for player in players:
        print player
        
#simple calculation to find levels of a binary tree
def CalcRounds(total):
    return math.ceil(math.log(total,2))

def PrintMatch(a, b, num):
    TopBox()
    print '\t  Match {2}\n\n\t{0} VS {1}'.format(a,b,num)
    BottomBox()
    
def IsEven(total):
    if (total % 2) == 0:
        return True
    else:
        return False

def BuildRounds(players):
    tPlayers = list(players)
    winners = []
    cnt=0
    
    #range from (0 - tPlayers) counting by 2 
    for i in range(0, len(tPlayers), 2):
        cnt+=1
        if len(players) != 1:
            PrintMatch(players.pop(),players.pop(),cnt)
            winners.append(tPlayers[i])
        else:
            #This will only be hit if players list is odd
            PrintMatch(players.pop(), 'BYE', cnt)
            winners.append(tPlayers[i])
        
    return winners
    
        
        
        
def BuildBracket(players):
    rounds = CalcRounds(amtPlayers)
    print '{} Rounds will be needed\n'.format(rounds)
    
    for round in range(int(rounds)):
        print 'Round {} '.format(round+1)
        winners = BuildRounds(players)
        
        if len(winners) == 1:
            print '{} is the winner!!!'.format(winners.pop())
            
        players = list(winners)
        
        

#Some list of players
listOfPlayers = ['Ozella', 'Ozie' ,'Pa', 'Pablo', 'Page',
'Paige','Palma','Palmer','Palmira','Pam', 'ano','asd']

#Some threshold to make sure program doen't burn and die
amtPlayers = len(listOfPlayers)
threshold = 100000
if amtPlayers > threshold:
    print 'warning list is too large'

#Randomize the players and build brackets
random.shuffle(listOfPlayers)
BuildBracket(listOfPlayers)
