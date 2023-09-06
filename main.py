import words
import random
def get_word():
    word = words.random_word
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")

    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                if word==word_completion:
                    print("Congrats, you guessed the word! You win!")
                    break
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1

            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")

        print(word_completion)
        print("\n")
    if word!=word_completion:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
    

    z = input("Do you want to play again(y/n)")
    if z == 'y' or z == 'Y':
        play(get_word())
play(get_word())