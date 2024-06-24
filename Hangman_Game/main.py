"""
Text-based Hangman Game in Python

This program implements the classic Hangman game in a text-based format.
The objective is to guess a randomly selected word by proposing one letter at a time.
The player has a limited number of incorrect guesses before losing the game.

Main features:
- Random selection of a word from a predefined list.
- Display of the word with underscores for unguessed letters.
- Input and validation of letter guesses from the player.
- Updating the word state with each correct guess.
- Tracking the number of incorrect guesses remaining.
- Detection of win and loss conditions with corresponding messages.

Author: Wided Belhouchet
"""
""" Import libraries """
import random
import hangman_stages
import word_file

""" Initialize player's lives """
lives = 6

""" Choose a random word from the list of words """
chosen_word = random.choice(word_file.words)
# Print the chosen word (useful for testing)
print(chosen_word)

""" Initialize display of the word to guess with underscores """
display = []
for i in range(len(chosen_word)):
    display += '_'
# Print initial state of the word to guess
print(display)

""" Initialize game: not over yet """
game_over = False

""" Main game loop """
while not game_over:
    """ Ask player to guess a letter """
    guessed_letter = input("Guess a letter: ").lower()

    """ Check each position in the chosen word """
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        """ If guessed letter matches a letter in the word """
        if letter == guessed_letter:
            display[position] = guessed_letter  # Update display

    print(display)  # Print current state of the word to guess after attempt

    """ If guessed letter is not in the chosen word, player loses a life """
    if guessed_letter not in chosen_word:
        lives -= 1
        """ If player has no lives left, game over and player loses """
        if lives == 0:
            game_over = True
            print("You Lose!")

    """ If all characters in the word have been guessed, player wins """
    if '_' not in display:
        game_over = True
        print("You win!")

    """ Print the hangman stage corresponding to remaining lives """
    print(hangman_stages.stages[lives])

""" End of game """

