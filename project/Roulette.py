import sys

try:
    with open(sys.argv[1], 'r') as fp:
        pass

except FileNotFoundError:
    print(f"No file called '{sys.argv[1]}' exists.")
    sys.exit()
except IndexError:
    print(f"Usage: {sys.argv[0]} <filename to open>")
    sys.exit()

def output_number_and_colour():
    from random import choice

    rows = []
    with open(sys.argv[1], 'r') as fp:
        for line in fp:
            columns = line.strip().split(",")
            if len(columns) == 2:
                rows.append(columns)

    random_row = choice(rows)
    random_number = int(random_row[0])
    random_colour = random_row[1].lower()

    return random_number, random_colour


def win_or_lose(number_input, colour_input, rand_number, rand_colour, user_bet_input, user_points):

    if number_input == rand_number and colour_input == rand_colour:
        bet_output = user_bet_input * 100
        user_points += bet_output - user_bet_input
        message = f'Well done! You guessed both the colour and the number so you win {bet_output} points!'

    elif colour_input == rand_colour:
        bet_output = user_bet_input * 2
        user_points += bet_output - user_bet_input
        message = f'Well done! You guessed the colour so you win {bet_output} points!'

    elif number_input == rand_number:
        bet_output = user_bet_input * 35
        user_points += bet_output - user_bet_input
        message = f'Well done! You guessed the number so you win {bet_output} points!'

    else:
        user_points -= user_bet_input
        message = 'Unlucky, try again!'

    return message, user_points


def play_the_game(return_history=False):
    user_points = 1000
    history = []

    def log(msg=''):
        print(msg)
        history.append(str(msg))

    while True:
        try:
            if user_points <= 0:
                log("You have run out of points. Game over!")
                log("Thank you for playing!")
                break
            else:
                log(f'\nYou currently have {user_points} points.')

            bet_input = int(input(f'Enter your bet: '))
            log("The bet you have chosen is: " + str(bet_input))
            if bet_input <= 0:
                log("Bet must be higher than 0 ")
                continue
            if bet_input > user_points:
                log("You cannot bet more points than you have.")
                continue

            number, colour = output_number_and_colour()
            num_input = int(input('Enter a number between 0 and 36: '))
            log("The number you have chosen is: " + str(num_input))
            if not (0 <= num_input <= 36):
                log('Please enter a number between 0 and 36.')
                continue

            color_input = input('Enter a colour (Red, Black or Green): ').lower()
            log("The colour you have chosen is: " + str(color_input))
            if color_input not in ('red', 'black', 'green'):
                log('Please enter a valid colour.')
                continue

            log(f'The ball landed on {number} ({colour}).')

            result, user_points = win_or_lose(num_input, color_input, number, colour, bet_input, user_points)
            log(result)
            log(f'You now have {user_points} points.')

            continue_or_not = input('Would you like to play again? (y/n): ')

            if continue_or_not.lower() == 'n':
                log(f'You have decided to stop playing.')
                log('Thank you for playing!')
                break
            elif continue_or_not.lower() == 'y':
                log(f'You have decided to keep playing! ')
                continue
            else:
                log('Illegal input, please enter y or n.')
                reply = input('Would you like to play again? (y/n): ')
        except ValueError:
            log('Please enter a number.')

    if return_history:
        return '\n'.join(history)
    return None


if __name__ == '__main__':

    transcript = play_the_game(return_history=True)
    if transcript is not None:
        with open('game.txt', 'w') as fp:
            fp.write(transcript)
        print("Transcript saved to game.txt")
