from collections import namedtuple
from fuzzywuzzy import fuzz

Problem = namedtuple('Problem', 'user_means bot_solve')


def analyze_text_message(message: str, db: list):
    """
    Lower all letter, call find and return possible solutions
    :param message: user message text str
    :param db: where we search errors, normal PROBLEMS and REAL_PHOTO_PROBLEM from problems_lib
    :return:
    """
    message = message.lower()
    possible_problems = find_possible_problem(message, [], db)
    return possible_problems


def find_possible_problem(message: str, possible_problems: list, db: list):
    """
    Find possible error using levinstein from fuzz lib
    :param message: message text
    :param possible_problems: the most likely problems
    :param db: with what compare
    :return:
    """
    max_dif = 0
    for case in db:
        cur_dif = fuzz.WRatio(message, case.lower())
        if cur_dif > max_dif:
            possible_problems = [(case, db[case])]
            max_dif = cur_dif
        elif cur_dif == max_dif:
            possible_problems.append((case, db[case]))
    return [] if max_dif == 0 else possible_problems
