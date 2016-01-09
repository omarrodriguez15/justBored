import random
import math


'''
Assuming we want random seed order meaning we can randomize
list right off the back. 

Single elimination no losers bracket

1.Determine if the list is even or odd
2.Then determine how many rounds there will be(how many levels on the tree)


EVEN
Levels are determined by log(n)


ODD


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


def BuildBracketEven(players):
    rounds = CalcRounds(amtPlayers)
    print '{} Rounds will be needed\n'.format(rounds)
    for round in range(int(rounds)):
        tPlayers = list(players)
        winners = []
        print 'Round {} '.format(round+1)
        
        cnt=0
        for i in range(0, len(tPlayers), 2):
            cnt+=1
            if len(players) != 1:
                PrintMatch(players.pop(),players.pop(),cnt)
                winners.append(tPlayers[i])
            else:
                PrintMatch(players.pop(), 'BYE', cnt)
                winners.append(tPlayers[i])
            
        if len(winners) == 1:
            print '{} is the winner!!!'.format(winners.pop())
        players = list(winners)
        


Originalplayers = ['Ozella', 'Ozie' ,'Pa', 'Pablo', 'Page',
'Paige','Palma','Palmer','Palmira','Pam', 'ano','asd']


amtPlayers = len(Originalplayers)

if amtPlayers > 100000:
    print 'warning list is too large'

random.shuffle(Originalplayers)
BuildBracketEven(Originalplayers)

'''
if IsEven(amtPlayers):
    BuildBracketEven(Originalplayers)
else:
    print 'List is not even totally freak out'
'''