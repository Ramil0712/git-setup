import random


def random_digit_foo():
    """The function returns random digit"""
    return str(random.randint(0, 11))


def digit_compare(hidden_key, entered_key):
    """ The function compare entered and hidden digits
        :param hidden_key: A digit randomly selected by computer
        :param entered_key:A digit entered by user
        :return: min, max or BINGO
    """
    # ADD TRY-EXCEPT BLOCK AND CONVERT HIDDEN AND ENTERED KEY TO INT AND CHECK TYPE
    answer = ''
    if hidden_key < entered_key:
        answer = 'Less'
    elif hidden_key > entered_key:
        answer = 'More'
    else:
        answer = 'BINGO'
    print(answer)
    return answer


def game_foo(hidden_key, entered_key=-1):
    """The function describes game algorythm. Return 0 if user press 'q',
    1 if user find a hidden digit"""
    try:
        while digit_compare(hidden_key, entered_key) != 'BINGO':
            if entered_key == 'q':
                return 0
            else:
                entered_key = str(input('Please enter a digit between 0 - 100 : '))
    except ValueError as e:
        print('Please enter a digit or "q" to quit game', e)
    return 1


def main_foo():
    """Main function"""
    hidden_key = random_digit_foo()
    entered_key = str(-1)
    if game_foo(hidden_key, entered_key) == 0:
        print('Game over')
        return
    else:
        return main_foo()


main_foo()


