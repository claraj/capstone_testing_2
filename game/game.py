import random


def main():

    choices = ['rock', 'paper', 'scissors']

    computer_play = choose_computer_play(choices)
    human_play = choose_human_play(choices)
    winner = determine_winner(human_play, computer_play, choices)
    print(f'Human chose {human_play} and computer chose {computer_play}. The results are:')
    if winner == 'tie':
        print('Tied game!')
    else:
        print(f'{winner} wins!')


def choose_computer_play(choices):
    computer_choice = random.choice(choices)
    return computer_choice


def choose_human_play(choices):
    message = ', '.join(choices)
    human_choice = input(f'Enter {message}: ')
    while human_choice not in choices:
        human_choice = input(f'Try again. Enter one of these choices {message}: ')
    return human_choice

def determine_winner(human_choice, computer_choice, valid_choices):
    
    # make sure both choices are valid
    if human_choice not in valid_choices:
        raise ValueError(f'Not a valid human play: {human_choice}')
    
    if computer_choice not in valid_choices:
        raise ValueError(f'Not a valid computer play: {computer_choice}')

    # Situations where the computer and human tie, by making the same choice
    if human_choice == computer_choice:
        return 'tie'

    # Situations where the human beats the computer

    elif human_choice == 'rock' and computer_choice == 'scissors':
        return 'human'

    elif human_choice == 'scissors' and computer_choice == 'paper':
        return 'human'

    elif human_choice == 'paper' and computer_choice == 'rock':
        return 'human'

    # If it's not a tie, and the human doesn't win, then the computer must the be winner.
    else:
        return 'computer'


if __name__ == '__main__':
    main()
