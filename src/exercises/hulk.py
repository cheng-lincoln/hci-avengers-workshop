from src.lib import next_alphabet

def crack(previous_guess):
    guess = [c for c in previous_guess]
    force_stop = False

    #=== Start writing your code from here onwards! ===
    # In this function, you are given (previous_guess).
    # Write code that uses (previous_guess) to make
    # a new (guess).
    # For debugging purposes, you can set (force_stop) = True
    # in order to force the loop to stop.

    # Example: If the (previous_guess) was 'agzz', your (next_guess) might be 'ahaa'.
    # Initially:
    # previous_guess[0] == guess[0] == 'a'
    # previous_guess[0] == guess[0] == 'g'
    # previous_guess[0] == guess[0] == 'z'
    # previous_guess[0] == guess[0] == 'z'
    # By the end of the function, (guess) should be:
    # guess[0] = 'a'
    # guess[1] = 'h'
    # guess[2] = 'a'
    # guess[3] = 'a'

    #=== Stop writing your code here! ===

    return (guess, force_stop)

