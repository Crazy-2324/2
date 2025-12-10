import random
r_words = ['python', 'java', 'kotlin', 'javascript','go','ruby','swift','c',]
word = random.choice(r_words)
game_over = False
print("Welcome to Hangman!")
print("Try to guess the programming language letter by letter.")
print("The word has","_"* len(word), "letters.")
correct_guesses = []
lives = 6
while not game_over:   
    guess = input("Guess the word: ").lower()
    display = ""
    for letter in word:
        if letter == guess:
            display += letter
            correct_guesses.append(guess)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"
    print(display)


    if "_" not in display:
        game_over = True
        print("You win!")
    if guess not in word:
        lives -= 1
        print(f"You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print("You lose! The word was:", word)