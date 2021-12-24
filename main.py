import os
import time
import random
from math import *


# functions for getting appropriate numbers
def get_natural_number(prompt: str):
    while True:
        try:
            _ = int(input(prompt))
            if _ > 0:
                break
            else:
                print('The entered value is not a "natural" number.')
        except ValueError:
            print('The entered value is not a number.')
    return _


def get_whole_number(prompt: str):
    while True:
        try:
            _ = int(input(prompt))
            if _ >= 0:
                break
            else:
                print('The entered value is not a whole number.')
        except ValueError:
            print('The entered value is not a whole number.')
    return _


def get_integer(prompt: str):
    while True:
        try:
            _ = int(input(prompt))
            break
        except ValueError:
            print('The entered value is not integral.')
    return _


def get_float(prompt: str):
    while True:
        try:
            _ = float(input(prompt))
            break
        except ValueError:
            print('The entered value is not a number.')
    return _


def subset_check(given, correct):
    x = given.split()
    y = correct.split()

    for index_of_word in range(len(x)):
        word = x[index_of_word]
        new_word = ''
        for letter in word:
            if letter.isalnum():
                new_word += letter
        x[index_of_word] = new_word

    for index_of_word in range(len(y)):
        word = y[index_of_word]
        new_word = ''
        for letter in word:
            if letter.isalnum():
                new_word += letter
        y[index_of_word] = new_word

    check1 = True
    check2 = True
    for a in x:
        check1 = a in y
    for b in y:
        check2 = b in x

    return check1 or check2


# game
code_for_clearing_terminal_output = "os.system('cls' if os.name == 'nt' else 'clear')"

while True:
    exec(code_for_clearing_terminal_output)
    name = input('Enter your name: ').capitalize()

    if name == 'Reset':
        if os.path.isfile('score.txt'):
            os.rename('score.txt', 'old_score.txt')
            print('Done.')
            time.sleep(2)
    elif name == 'Restore':
        if os.path.isfile('old_score.txt'):
            os.rename('old_score.txt', 'score.txt')
            print('Done.')
            time.sleep(2)
    else:
        break


set_of_questions_and_answers = {'Governor of RBI: ': 'Shakti Kanta Das',
                                'LPG is the abbreviation for: ': 'Liquefied Petroleum Gas',
                                'CEO of Microsoft: ': 'Satya Nadella', 'First female PM of India: ': 'Indira Gandhi',
                                'Longest bone in the body: ': 'Femur',
                                'What has to be broken before you can use it: ': 'Egg',
                                'I’m tall when I’m young, and I’m short when I’m old. What am I: ': 'Candle',
                                'What is full of holes but still holds water: ': 'Sponge',
                                'What is always in front of you but can’t be seen: ': 'Future',
                                'There’s a one-story house in which everything is yellow. \
Yellow walls, yellow doors, yellow furniture. What color are the stairs: ': 'No stairs',
                                'What can you break, even if you never pick it up or touch it: ': 'Promise',
                                'What goes up but never comes down: ': 'Age',
                                "A man who was outside in the rain without an umbrella or \
hat didn’t get a single hair on his head wet. How: ": 'He was bald', 'What gets wet while drying: ': 'Towel',
                                'What can you keep after giving to someone: ': 'Your word',
                                'I shave every day, but my beard stays the same. What am I: ': 'Barber',
                                'Where does today come before yesterday: ': 'Dictionary',
                                'There’s a one-story house where everything is yellow. The walls are yellow.\
 The doors are yellow. All the furniture is yellow. The house has yellow beds and yellow couches.\
 What color are the stairs?: ': 'There are no stairs it’s a one-story house',
                                'What four-letter word can be written forward, backward, or upside down,\
 and can still be read from left to right?: ': 'NOON',
                                'Name three consecutive days without naming any of the seven days of the week.: ':
                                    'Yesterday today and tomorrow',
                                'You are in a dark room with a box of matches. On a table are a candle,\
 an oil lamp, and a log of firewood. What do you light first?: ': 'The match - Can’t light any of those things without \
 a lit match', 'Three doctors all say Robert is their brother. Robert says he has no brothers. Who is lying?: ':
                                    "No one the doctors are Robert's sisters",
                                ' A man is holding exactly $5.25, but only has one coin. How is this possible?: ':
                                    'He has a quarter and a $5 bill',
                                'I called my dog from the opposite side of the river. The dog crossed the river without\
 getting wet, and without using a bridge, a boat, or a raft. How is that possible?: ': 'The river was frozen',
                                'What two words, added together, contain the most letters?: ': 'Post office',
                                'Bella is outside a shop. She can’t read the signs, but she knows she needs to go in to\
 make a purchase. What store is she at?: ': 'An eyeglasses store',
                                'Wednesday, Bill and Jim went to a restaurant they ordered and ate their food and stuff\
 like that. Then they paid the bill, but neither Bill nor Jim paid the bill. Who did?: ': 'Wednesday did',
                                'A man was driving his truck. His lights weren’t on. The moon was not out.\
 There were no streetlights. Up ahead, a woman was crossing the street. Luckily, the truck driver stopped in time—how\
 did he see her?: ': 'It was daytime',
                                'A horse attached to a 24-foot chain wants an apple that is 26 feet away.\
 He reaches the apple and munches on it no problem—how is that possible?: ':
                                    'The other end of the chain isn’t attached to anything'}
points_for_untimed = 20
set_of_timed_questions_and_answers_5s = {"(2 + 2 / 2): ": 3, '(1 + 1): ': 2, 'Number of Vedas: ': 4,
                                         '(36 x 70): ': 2520, '(23675 * 12 * 12428 * 0 * 12987 / 5 ): ': 0,
                                         'What month of the year has 28 days: ': 'All',
                                         'What has many keys but can’t open a single lock: ': 'Piano',
                                         'Mississippi has four S’s and four I’s. Can you spell \
that without using S or I?: ': 'that',
                                         'Grandpa went out for a walk and it started to rain. He didn’t bring an \
umbrella or a hat. His clothes got soaked, but not a hair on his head was wet. How is this possible?: ': 'Grandpa’s \
bald', 'What is at the end of the rainbow?: ': 'The letter W', 'What word is always spelled wrong?: ': 'Wrong',
                                         'Which letter of the alphabet has the most water?: ': 'The C',
                                         'I have married many times, but have always been single. Who am I?: ': 'A \
priest', 'I am easy to lift but hard to throw. What am I?: ':
                                             'A feather - A piece of paper or a leaf would certainly qualify too',
                                         'What type of cheese is made backward?: ': 'Edam',
                                         'An electric train is headed east. Where does the smoke go?: ':
                                             'Electric trains don’t produce any smoke',
                                         'What is the one thing everyone can agree is between heaven and earth?: ':
                                             'The word and', 'What has a bottom at the top?: ': 'Your legs',
                                         'If you drop a yellow hat in the Red Sea, what does it become?: ': 'Wet',
                                         'What tastes better than it smells?: ': 'Your tongue',
                                         'Which word becomes shorter when you add 2 letters to it?: ': 'Short'}
set_of_timed_questions_and_answers_10s = {'David’s parents have three sons: Snap, Crackle, \
and what’s the name of the third son: ': 'David',
                                          'The more of this there is, the less you see. What is it: ': 'Darkness',
                                          'What gets bigger when more is taken away: ': 'Hole',
                                          'A girl fell off a 20-foot ladder. She wasn’t hurt. How?: ':
                                              'She fell off the bottom step',
                                          'You’re in a race and you pass the person in second place. \
What place are you in now?: ': 'Second place', 'Two people were playing chess. They both won. How is this possible?: ':
                                              'They were playing two different games against other opponents',
                                          'What invention lets you look right through a wall?: ': 'A window',
                                          'Where does today come before yesterday?: ': 'In the dictionary',
                                          'What kind of ship has two mates but no captain?: ': 'A relationship',
                                          'You can hold me in your left hand but not your right. What am I?: ':
                                              'Your right elbow or hand',
                                          'I go around all the places, cities, towns, and villages, \
but never come inside. What am I?: ': 'A street', 'You go at red and stop at green. What am I?: ': 'A watermelon',
                                          'I am higher without a head. What am I?: ': 'A pillow',
                                          'I have 13 hearts, but no lungs or stomach. What am I?: ': 'A deck of cards',
                                          'I break, but never fall. And I fall, but never break. What are we?: ':
                                              'Day and night',
                                          'What are the next three letters in this sequence: O, T, T, F, F, S, S—what \
comes next?: ': 'E N T The letters are the first letters of the written numbers one, two, three, four, five, etc. \
“Eight, nine, ten” are next.', 'How can you physically stand behind your father while he is standing behind you?: ':
                                              'You and your father are standing back to back',
                                          'A girl throws a ball as hard as she can. \
It comes back to her, even though nothing and nobody touches it. How?: ': 'She throws it straight up in the air',
                                          'When is “L” greater than “XL”?: ': 'When you’re using Roman numerals',
                                          'How can the number four be half of five?: ':
                                              'IV the Roman numeral for four is “half” (two letters) of the word five.',
                                          'What color is the wind?: ': 'Blew',
                                          'What can jump higher than a building?: ':
                                              'Anything that can jump - buildings can’t jump',
                                          'What has four wheels and flies?: ': 'A garbage truck',
                                          'A monkey, a squirrel, and a bird are racing to the top of a coconut tree. \
Who will get the banana first?: ': 'None of them - coconut trees don’t produce bananas',
                                          'I can be cracked, I can be made. I can be told, \
I can be played. What am I?: ': 'A joke'}
max_points_for_timed = 50

# creating a combined dictionary of Q&A
all_questions = {}
all_questions.update(set_of_questions_and_answers)
all_questions.update(set_of_timed_questions_and_answers_5s)

# obtaining past scoreboard and checking whether it's the first time running the game
already_played = os.path.isfile('score.txt')
obtainment_method = 'r' if already_played else 'w+'
with open('score.txt', obtainment_method) as score_file:
    lines = score_file.readlines()  # name: score.txt
    scoreboard = {}
    for line in lines:
        line = line.strip()
        split_line = line.split(': ')
        scoreboard[split_line[0]] = int(split_line[1])
    scoreboard_empty = not scoreboard


def display_tutorial(to_delay=True):
    delay = 1.5 if to_delay else 0.25
    instructions = ['Welcome to Pyzzle.', 'This is a puzzle game, coded entirely in Python.',
                    'You will be given a series of questions, which you have to answer correctly.',
                    'In some of the questions, you also might have to answer within the given time limit, else you will\
 lose.', 'The objective is to answer all the questions correctly in the least time.', 'Get Ready.']
    for instruction in instructions:
        time.sleep(delay)
        exec(code_for_clearing_terminal_output)
        print(instruction)
        time.sleep(delay)
    exec(code_for_clearing_terminal_output)


player_highest_score = 0
if scoreboard_empty:
    display_tutorial()
elif name in scoreboard:
    exec(code_for_clearing_terminal_output)
    player_highest_score = scoreboard[name]
    print(f'Your highest score yet is {player_highest_score} points.')
    time.sleep(2)
    exec(code_for_clearing_terminal_output)

current_score = 0


def ask():
    global current_score, questions_to_ask, to_ask
    if not questions_to_ask:
        to_ask = False
        exec(code_for_clearing_terminal_output)
        print("You have completed the game!")
        time.sleep(3)
        print("You can now try to answer the questions quicker to get a higher score.")
        time.sleep(5)
        exec(code_for_clearing_terminal_output)
        return None
    question_no = random.randint(0, len(questions_to_ask) - 1)
    question = list(questions_to_ask.keys())[question_no]
    correct_answer = questions_to_ask[question]
    del questions_to_ask[question]
    if question in set_of_timed_questions_and_answers_5s:
        time_limit = 5
    elif question in set_of_timed_questions_and_answers_10s:
        time_limit = 10
    else:
        time_limit = 0
    current_score += ask_subprocess(question, correct_answer, time_limit)


def ask_subprocess(question, correct_answer, time_limit):
    global to_ask
    exec(code_for_clearing_terminal_output)
    start_time = time.time()
    q_message = question[:-2] + f'[{time_limit} seconds]: ' if time_limit > 0 else question
    if isinstance(correct_answer, str):
        correct_answer = correct_answer.lower()
        answer = input(q_message).lower()
        if subset_check(answer, correct_answer):
            answer = correct_answer
    elif isinstance(correct_answer, int):
        answer = get_integer(q_message)
    elif isinstance(correct_answer, float):
        answer = get_float(q_message)
    else:
        answer = None

    end_time = time.time()
    time_taken = floor(end_time - start_time)
    if time_limit != 0:
        time.sleep(0.25)
        exec(code_for_clearing_terminal_output)
        message = f'You answered in {time_taken} seconds.' if time_taken < time_limit else "You took too much time!"
        print(message)
    if time_limit == 0 and answer == correct_answer:
        time.sleep(2)
        exec(code_for_clearing_terminal_output)
        print("Your answer is correct.")
        points_to_add = points_for_untimed
    elif answer == correct_answer and time_taken < time_limit:
        time.sleep(2)
        exec(code_for_clearing_terminal_output)
        print("Your answer is correct.")
        points_to_add = round(max_points_for_timed * (time_limit - time_taken) / time_limit)
    elif time_taken < time_limit:
        time.sleep(2)
        exec(code_for_clearing_terminal_output)
        print("Your answer is wrong.")
        print(f'The correct answer is: {correct_answer}')
        points_to_add = 0
        to_ask = False
    else:
        if answer == correct_answer:
            pass
        else:
            print("Your answer is wrong.")
            print(f'The correct answer is: {correct_answer}')
        points_to_add = 0
        to_ask = False
    time.sleep(2)
    return points_to_add


while True:
    exec(code_for_clearing_terminal_output)
    selection = input(f'''Select one of the following: 
    Play
    Tutorial
    Scoreboard
    Quit\n\n>>> ''').lower()

    exec(code_for_clearing_terminal_output)

    if selection == 'play':
        questions_to_ask = all_questions
        to_ask = True
        while to_ask:
            ask()
        print('Your Score: ' + str(current_score))
        time.sleep(2)
        if current_score > player_highest_score:
            exec(code_for_clearing_terminal_output)
            print('This is your new high score.')
            player_highest_score = current_score
        current_score = 0
        scoreboard[name] = player_highest_score
        scoreboard_names_arranged = sorted(scoreboard, key=lambda key: scoreboard[key], reverse=True)
        temp = {}
        for player in scoreboard_names_arranged:
            temp[player] = scoreboard[player]
        scoreboard = dict(temp)
        temp = None
        with open('score.txt', 'w+') as score_file:
            lines_to_write = []
            for player in scoreboard:
                lines_to_write += [f'{player}: {scoreboard[player]}\n']
            score_file.writelines(lines_to_write)
        with open('score.txt', 'r') as score_file:
            lines = score_file.readlines()
            scoreboard = {}
            for line in lines:
                line = line.strip()
                split_line = line.split(': ')
                scoreboard[split_line[0]] = int(split_line[1])
            scoreboard_empty = not scoreboard
    elif selection == 'tutorial':
        display_tutorial()
    elif selection == 'scoreboard':
        with open('score.txt', 'w+') as score_file:
            lines_to_write = []
            for player in scoreboard:
                lines_to_write += [f'{player}: {scoreboard[player]}\n']
            score_file.writelines(lines_to_write)
        with open('score.txt', 'r') as score_file:
            lines = score_file.readlines()
            scoreboard = {}
            for line in lines:
                line = line.strip()
                split_line = line.split(': ')
                scoreboard[split_line[0]] = int(split_line[1])
            scoreboard_empty = not scoreboard
        if not scoreboard_empty:
            for name in scoreboard:
                print(f'{name}: {scoreboard[name]}')
        else:
            print('No scores yet.')
        time.sleep(5)
    elif selection == 'quit':
        with open('score.txt', 'w+') as score_file:
            lines_to_write = []
            for player in scoreboard:
                lines_to_write += [f'{player}: {scoreboard[player]}\n']
            score_file.writelines(lines_to_write)
        with open('score.txt', 'r') as score_file:
            lines = score_file.readlines()
            scoreboard = {}
            for line in lines:
                line = line.strip()
                split_line = line.split(': ')
                scoreboard[split_line[0]] = int(split_line[1])
            scoreboard_empty = not scoreboard
        break
    elif selection == 'reset':
        with open('score.txt', 'w+') as score_file:
            lines_to_write = []
            for player in scoreboard:
                lines_to_write += [f'{player}: {scoreboard[player]}\n']
            score_file.writelines(lines_to_write)
        with open('score.txt', 'r') as score_file:
            lines = score_file.readlines()
            scoreboard = {}
            for line in lines:
                line = line.strip()
                split_line = line.split(': ')
                scoreboard[split_line[0]] = int(split_line[1])
            scoreboard_empty = not scoreboard
        os.rename('score.txt', 'old_score.txt')
        break
    else:
        print('Invalid Command.')
    time.sleep(2)
    exec(code_for_clearing_terminal_output)
