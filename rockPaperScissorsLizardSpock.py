
import random 

vals = {
    'Rock': {
      'Scissors': 'Crushes',
      'Lizard':'Crushes'
    },
    'Paper': {
      'Rock': 'Covers',
      'Spock':'Disproves'
    },
    'Scissors': {
        'Paper': 'Cuts',
        'Lizard': 'Decapitates'
    },
    'Lizard': {
        'Spock': 'Poisons',
        'Paper': 'Eats'
    },
    'Spock': {
        'Rock': 'Vaporizes',
        'Scissors': 'Smashes'
    }
}

# generate random for easy run 
a = random.choice(list(vals.keys()))
b = random.choice(list(vals.keys()))

#a = input('Player1 enter Rock, Paper, Scissors, Lizard or Spock: ')
#b = input('Player2 enter Rock, Paper, Scissors, Lizard or Spock: ')

print('User selected: ' + a )
print('Computer selected: ' + b)

if b in vals[a]:
    print('User wins! ' + a + ' ' + vals[a][b] +  ' ' + b)
elif a in vals[b]:
    print('Computer wins! ' + b + ' ' + vals[b][a] + ' ' + a)
else:
    print('Try Again')
