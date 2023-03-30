import random


def letter_show_foo(hidden_word, entered_key, word_template):
    """The function shows letter in the hidden word if it is there"""
    for i in range(len(hidden_word)):
        if hidden_word[i] == entered_key:
            word_template[i] = entered_key
    print("Hidden word :", word_template)
    return word_template


def random_word_foo():
    word_dict = ('mama', 'papa', 'girl', 'boy')
    """The function returns random word"""
    return str(random.choice(word_dict))


def letter_check_foo(hidden_word, entered_key, word_template):
    """ The function compare entered and hidden digits
        :param hidden_word: A word randomly selected by computer
        :param entered_key:A letter entered by user
        :param word_template is a mask of hidden word
        :return: answer and "-1" - when letter not found,
                 "1" -when at least one letter found, but whole word is not.
                  10 - when all letters found
    """
    answer = ''
    answer = letter_show_foo(hidden_word, entered_key, word_template)
    if entered_key not in hidden_word:
        # if '*' in answer:
        #     return answer
        # else:
        #     return answer
    # else:
        answer = word_template
        print('One life is gone')
    # print("Hidden word :", answer)
    return answer



def game_foo(word):
    """The function describes game algorythm.
    Return: 0 if user quit,
            1 if user left all his lifes,
            10 if user find a hidden word"""
    hidden_word = [*word]
    life_counter = 10
    word_template = ['*'] * len(hidden_word)
    print(word_template, sep=' ')
    try:
        entered_letter = str(input('Please enter a letter : '))
        while letter_check_foo(hidden_word, entered_letter, word_template) != hidden_word and life_counter > 1:
            if entered_letter == 0:
                return 0
            elif life_counter == 0:
                return 1
            else:
                if entered_letter not in hidden_word:
                    life_counter -= 1
                    print(life_counter, " lifes left")
                entered_letter = str(input('Please enter a letter : '))
    except ValueError as e:
        print('Please enter a letter or 0 to quit game', e)
    return 10


def main_foo():
    """Main function"""
    hidden_word = random_word_foo()
    game_var = game_foo(hidden_word)
    if game_var == 0:
        print('Game over')
        return
    elif game_var == 1:
        print('YOU LOSE. The word was a ' + hidden_word)
    else:
        print('YOU WIN. The word was a ' + hidden_word)
        return main_foo()


main_foo()
