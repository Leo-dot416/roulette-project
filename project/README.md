# Project

This is a casino Roulette game-like 

### How it works:

- The user starts with 1000 points
- Each round they:
  - Place a bet
  - Guess a number (0-36)
  - Guess a colour (red, black or green)
- The program:
  - Randomly selects a real wheel outcome from the data file provided (roulette_100_rounds.cvs)
  - Decides how many points the user wins and loses
  - Prints and logs everything to a game.txt file

### How to run the program:

- From command line:
  - `python (or python3) Roulette.py roulette_100_rounds.csv `

- If:
  - The file doesn't exist the program prints:
    *No file called 'filename' exists.* and exits
  - You forget to pass a filename the program prints:
    *Usage: Roulette.py <filename to open>* and exits

### Results given by program:

- If number and colour are correct, you win x100 of your bet
- If only number is correct, you win x35 of your bet
- If only colour is correct, you win x2 of you bet
- If nothing is correct, you lose the bet

### Game will end if:

- The user runs out of points
- The user chooses not to continue

