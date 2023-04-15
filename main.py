import random

EASY = 10
HARD = 5

correct_answer = random.randint(0, 101)


def guessing_game():
    global correct_answer, EASY, HARD
    print(
        'Welcome to the Number Guessing Game! \n I\'am thinking of a number between 1 and 100'
    )
    print(f'Psst, the correct answer is {correct_answer}')
    should_continue = True

    while should_continue:
        diff = input('Choose difficulty. Type "easy" or "hard": ').lower()
        if diff == 'easy':
            print(f'You have {EASY} attempts remaining to guess the number')
            for i in range(0, EASY):
                guess = int(input('Make a guess: '))
                if correct_answer > guess:
                      EASY = EASY - 1
                      if EASY == 0:
                          print(f'Game Over! Correct answer is {correct_answer}')
                          should_continue = False
                      else:
                          print('Too low \nGuess again.')
                          print(
                              f'You have {EASY} attempts remaining to guess the number')
                elif correct_answer < guess:
                      EASY = EASY - 1
                      if EASY == 0:
                          print(f'Game Over! Correct answer is {correct_answer}')
                          should_continue = False
                      else:
                          print('Too high \nGuess again.')
                          print(
                              f'You have {EASY} attempts remaining to guess the number')

                elif correct_answer == guess:
                      should_continue = False
                      print('You won!')
                      again = input('Do you want to play again?: y/n ')
                      if again == 'n':
                        should_continue = False
                      else:
                        guessing_game()
        if diff == 'hard':
            print(f'You have {HARD} attempts remaining to guess the number')
            for i in range(0, HARD):
                  guess = int(input('Make a guess: '))
                  if correct_answer > guess:
                      HARD = HARD - 1
                      if HARD == 0:
                          print(f'Game Over! Correct answer is {correct_answer}')
                          should_continue = False
                      else:
                          print('Too low \nGuess again.')
                          print(
                              f'You have {HARD} attempts remaining to guess the number'
                          )
                  elif correct_answer < guess:
                      HARD = HARD - 1
                      if HARD == 0:
                          print(f'Game Over! Correct answer is {correct_answer}')
                          should_continue = False
                      else:
                          print('Too high \nGuess again.')
                          print(
                              f'You have {HARD} attempts remaining to guess the number'
                          )
                  elif correct_answer == guess:
                      should_continue = False
                      print('You won!')
                      again = input('Do you want to play again?: y/n ')
                      if again == 'n':
                        should_continue = False
                      else:
                        guessing_game()


guessing_game()