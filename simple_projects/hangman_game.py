import random

print("Let's Play Hangman!!!")
print("You have only 6lives i.e you are allowed a wrong guess for just 6 times!  GOOD LUCK...")


def get_word():
    word_list = ["python", "java", "javascript", "ruby", "php"]
    return random.choice(word_list)


def play_game():
    word = get_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that letter. Guess another letter.')
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('Sorry, you died. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')


play_game()
