import random


computer_score = 0
player_score = 0

choices = ('ROCK', 'PAPER', 'SCISSORS')

while computer_score + player_score != 5:
    
    computer = random.choice(choices)
    player = input('ROCK, PAPER, SCISSORS! ').upper()
        
        
    if player == computer:
        print (f'Player: {player} vs Computer: {computer}')
        print ('Tie\n')
        
    
    #Rock vs. Paper
    elif player == 'ROCK' and computer == 'PAPER':
        print (f'Player: {player} vs Computer: {computer}')
        print ('Winner : Player\n')
        player_score += 1
        
        
    #Rock Vs. Scissors    
    elif player == 'ROCK' and computer == 'SCISSORS':
        print (f'Player: {player} vs Computer: {computer}')
        print ('Winner : Player\n')
        player_score += 1
        
        
    #Scissors Vs. Paper
    elif player == 'SCISSORS' and computer == 'PAPER':
        print (f'Player: {player} vs Computer: {computer}')
        print ('Winner : Player\n')
        player_score += 1
        
    #IF INVALID INPUT    
    elif player not in choices:
        print ('Invalid input. Type ROCK, PAPER, SCISSORS only.\n')
        
    else:
        computer_score += 1
        print (f'Player: {player} vs Computer: {computer}')
        print ('Winner : Computer\n')
        

if computer_score > player_score:
    print ('Defeated!')
else:
    print ('Congratulations!')
