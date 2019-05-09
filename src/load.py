import json
from collections import namedtuple

HULK = 'hulk'
STRANGE = 'strange'
THANOS = 'thanos'

EXERCISES = [HULK, STRANGE, THANOS]

STRANGE_INTERVAL_S = 0.1

def load_answers():
    with open('resources/config.json') as fp:
        exercises = json.load(fp)
    answers = namedtuple('answers', EXERCISES)
    return answers(exercises[HULK]['sha1'], exercises[STRANGE]['sha1'], exercises[THANOS]['sha1'])

def load_rainbow_table():
    with open('resources/rainbow_table.txt') as fp:
        return fp.read().split('\n')
