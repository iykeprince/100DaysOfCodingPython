import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6 

print(logo)

choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. 
    print(f"****************** {lives}/6 LIVES LEFT ***********************")
    guess = input('Guess a letter: ').lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    # TODO-3 - Check if the letter the user guessed (guess) is one of hte letter in choosen word. Print "Right" if it is and "Wrong" if it is not. 
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in choosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. ")
        
        if lives == 0:
            game_over = True
            print(f"***************IT WAS {choosen_word}! YOU LOSE ****************")

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("********************YOU WIN********************")