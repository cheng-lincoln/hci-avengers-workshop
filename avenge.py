import sys
sys.dont_write_bytecode = True

from src.exercises.hulk import crack as hulk_crack
from src.exercises.strange import crack as strange_crack
from src.exercises.thanos import crack as thanos_crack
from src.load import load_answers, HULK, STRANGE, THANOS, EXERCISES, STRANGE_INTERVAL_S
from src.lib import sha1_digest, input_multiple_choice, vc_input
import time

input_map = {
    'script': True,
    'manual': False
}

def check_password(clear_text, sha1_password):
    if isinstance(clear_text, list):
        clear_text = ''.join(clear_text)
    return sha1_digest(clear_text) == sha1_password

def check_guess(exercise, guess, answers):
    if exercise == HULK:
        return check_password(guess, answers.hulk)
    if exercise == STRANGE:
        for (g, a) in zip(guess, answers.strange):
            time.sleep(STRANGE_INTERVAL_S)
            if not check_password(g, a):
                return False
        return True
    if exercise == THANOS:
        return check_password(guess, answers.thanos)

def execute_crack(exercise, controls):
    if exercise == HULK:
        return hulk_crack(controls['guess'])
    if exercise == STRANGE:
        return strange_crack(controls['guess'], time.time() - controls['last_timestamp'])
    if exercise == THANOS:
        return thanos_crack(controls['guess'], controls['tries'])

if __name__ == '__main__':
    exercise = input_multiple_choice('Choose exercise', EXERCISES)
    input_method = input_multiple_choice('Choose input method', list(input_map))

    use_script = input_map[input_method]

    answers = load_answers()

    controls = {
        'guess': ['a', 'a', 'a', 'a'],
        'last_timestamp': time.time(),
        'tries': 0,
        'solved': False,
        'stop': False,
    }

    while not controls['solved']:
        (guess, force_stop) = execute_crack(exercise, controls) if use_script else (vc_input('Password: '), False)
        controls['last_timestamp'] = time.time()
        controls['tries'] += 1
        controls['solved'] = check_guess(exercise, guess, answers)
        controls['guess'] = guess
        if not controls['solved']:
            print('{0} (wrong)'.format(''.join(guess)))
        if force_stop or controls['solved']:
            break

    if controls['solved']:
        print('Solved: {0} in {1} tries'.format(''.join(controls['guess']), controls['tries']))
    else:
        print(':(')