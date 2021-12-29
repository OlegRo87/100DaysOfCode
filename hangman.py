import hangman_words
import hangman_art
import random
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(f'Print, the solution is {chosen_word}.')
display = []
word_length = len(chosen_word)
lives = 6
for _ in range(word_length):
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for index in range(word_length):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter


    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])
