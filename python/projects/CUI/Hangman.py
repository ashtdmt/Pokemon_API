#Hangman game program

import random
def choose_word():
    """Randomly selects a word from a predefined list."""
    words = ["python", "hangman", "programming", "challenge", "developer"]
    return random.choice(words)
def display_hangman(tries):
    """Returns the hangman ASCII art based on the number of tries left."""
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           
           
           
           
           
        """,
    ]
    return stages[tries]    

def play_hangman():
    """Main function to play the Hangman game."""
    word = choose_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        guess = input("Please enter a letter or a word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print("Incorrect guess.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job! You guessed a letter.")
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word.")
            elif guess != word:
                print("Incorrect guess.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid input. Please try again.")

        print(display_hangman(tries))
        print(word_completion)

    if guessed:
        print(f"Congratulations! You guessed the word '{word}' correctly!")
    else:
        print(f"Sorry, you ran out of tries. The word was '{word}'.")

def main():
    """Entry point for the Hangman game."""
    play_hangman()
    while input("Do you want to play again? (y/n): ").lower() == 'y':
        play_hangman()
    print("Thanks for playing Hangman!")
if __name__ == "__main__":  
    main()
